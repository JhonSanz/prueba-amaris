from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_elasticloadbalancingv2 as elbv2,
    aws_dynamodb as dynamodb,
    aws_iam as iam,
)
from constructs import Construct


class IacStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # VPC
        vpc = ec2.Vpc(self, "MyVpc", max_azs=2)

        table_fund = dynamodb.Table(
            self,
            "AmarisFundTable",
            table_name="amaris-fund",  # Nombre de la tabla
            partition_key=dynamodb.Attribute(
                name="fundId", type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
        )

        table_transaction = dynamodb.Table(
            self,
            "AmarisTransactionTable",
            table_name="amaris-transaction",  # Nombre de la tabla
            partition_key=dynamodb.Attribute(
                name="userId", type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
        )

        table_users = dynamodb.Table(
            self,
            "AmarisUsersTable",
            table_name="amaris-users",  # Nombre de la tabla
            partition_key=dynamodb.Attribute(
                name="userId", type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
        )

        dynamodb_policy_fund = iam.PolicyStatement(
            actions=["dynamodb:*"],
            resources=[table_fund.table_arn],
        )
        
        dynamodb_policy_transaction = iam.PolicyStatement(
            actions=["dynamodb:*"],
            resources=[table_transaction.table_arn],
        )
        
        dynamodb_policy_users = iam.PolicyStatement(
            actions=["dynamodb:*"],
            resources=[table_users.table_arn],
        )

        # ECS Cluster
        cluster = ecs.Cluster(self, "MyCluster", vpc=vpc)

        # Rol de ejecución de la tarea
        backend_task_role = iam.Role(
            self,
            "BackendTaskRole",
            assumed_by=iam.ServicePrincipal("ecs-tasks.amazonaws.com"),
            inline_policies={
                "DynamoDBAccess": iam.PolicyDocument(statements=[
                    dynamodb_policy_fund,
                    dynamodb_policy_transaction,
                    dynamodb_policy_users
                ])
            },
        )

        # FastAPI Backend - Fargate Task Definition
        backend_task = ecs.FargateTaskDefinition(
            self, "BackendTask", task_role=backend_task_role
        )
        backend_container = backend_task.add_container(
            "BackendContainer",
            image=ecs.ContainerImage.from_registry("jhonsanz/amaris-prueba:backend"),
            memory_limit_mib=512,
            cpu=256,
            logging=ecs.LogDriver.aws_logs(stream_prefix="backend"),
        )
        backend_container.add_port_mappings(
            ecs.PortMapping(container_port=8000)
        )  # Se quita el host_port

        # React Frontend - Fargate Task Definition
        frontend_task = ecs.FargateTaskDefinition(self, "FrontendTask")
        frontend_container = frontend_task.add_container(
            "FrontendContainer",
            image=ecs.ContainerImage.from_registry("jhonsanz/amaris-prueba:frontend"),
            memory_limit_mib=512,
            cpu=256,
            logging=ecs.LogDriver.aws_logs(stream_prefix="frontend"),
        )
        frontend_container.add_port_mappings(
            ecs.PortMapping(container_port=80)
        )  # Se quita el host_port

        # Create ALB
        lb = elbv2.ApplicationLoadBalancer(self, "LB", vpc=vpc, internet_facing=True)

        listener = lb.add_listener("PublicListener", port=80, open=True)

        # Fargate Service for Backend
        backend_service = ecs.FargateService(
            self,
            "BackendService",
            cluster=cluster,
            task_definition=backend_task,
            desired_count=1,
            assign_public_ip=True,  # Asigna una IP pública
        )

        # Create backend target group explicitly
        backend_target_group = listener.add_targets(
            "BackendTarget",
            port=8000,
            targets=[backend_service],
            health_check=elbv2.HealthCheck(path="/fund/health"),
        )

        # Fargate Service for Frontend
        frontend_service = ecs.FargateService(
            self,
            "FrontendService",
            cluster=cluster,
            task_definition=frontend_task,
            desired_count=1,
            assign_public_ip=True,  # Asigna una IP pública
        )

        # Create frontend target group explicitly
        frontend_target_group = listener.add_targets(
            "FrontendTarget",
            port=80,
            targets=[frontend_service],
            health_check=elbv2.HealthCheck(path="/"),
        )

        # Configura la variable de entorno REACT_APP_API_URL
        frontend_container.add_environment(
            "REACT_APP_API_URL",  # Nombre de la variable de entorno
            f"http://{lb.load_balancer_dns_name}",  # URL del Load Balancer
        )

        # Crear reglas de enrutamiento para el listener
        listener.add_action(
            "DefaultActionForFrontend",
            action=elbv2.ListenerAction.forward([frontend_target_group]),
        )

        listener.add_action(
            "ApiActionForBackend",
            action=elbv2.ListenerAction.forward([backend_target_group]),
            conditions=[
                elbv2.ListenerCondition.path_patterns(
                    ["/fund/*"]
                )  # Redirige solicitudes a /api al backend
            ],
            priority=1
        )
