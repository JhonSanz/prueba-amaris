from fastapi import HTTPException
import boto3
from botocore.exceptions import ClientError


def get_db():
    try:
        dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
        return dynamodb
    except ClientError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al conectar con DynamoDB: {e.response['Error']['Message']}",
        )
