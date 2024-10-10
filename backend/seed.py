import boto3

# Inicializar el cliente de DynamoDB
dynamodb = boto3.resource("dynamodb")

# Datos para la tabla amaris-fund
fund_data = [
    {
        "fundId": "1",
        "amount": 75000,
        "category": "FPV",
        "name": "FPV_EL CLIENTE_RECAUDADORA",
    },
    {
        "fundId": "2",
        "amount": 125000,
        "category": "FPV",
        "name": "FPV_EL CLIENTE_ECOPETROL",
    },
    {"fundId": "3", "amount": 50000, "category": "FIC", "name": "DEUDAPRIVADA"},
    {"fundId": "4", "amount": 250000, "category": "FIC", "name": "FDO-ACCIONES"},
    {
        "fundId": "5",
        "amount": 100000,
        "category": "FPV",
        "name": "FPV_EL CLIENTE_DINAMICA",
    },
]

# Datos para la tabla amaris-users
users_data = [
    {
        "userId": "user_001",
        "money": 500000,
        "name": "Cliente feliz",
        "subscriptions": [],
    }
]


# Función para poblar una tabla de DynamoDB
def populate_table(table_name, items):
    table = dynamodb.Table(table_name)
    with table.batch_writer() as batch:
        for item in items:
            batch.put_item(Item=item)
    print(f"Datos insertados en la tabla {table_name}")


# Poblar la tabla amaris-fund
populate_table("amaris-fund", fund_data)

# Poblar la tabla amaris-users
populate_table("amaris-users", users_data)
