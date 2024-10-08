from uuid import uuid4
from datetime import datetime
from app.api.schemas.fund import FundSubscribe
from app.api.schemas.transaction import Transaccion
import boto3


def fund_subscribe_db(*, transaction: Transaccion, db):
    table = db.Table("amaris")
    transaction_date = datetime.now().isoformat()

    item = {
        "PK": f"Usuario#1",
        "SK": f"TRANSACCION#{transaction_date}",
        "TipoEntidad": "TRANSACCION",
        "FondoID": transaction.fondo_id,
        "FondoNombre": transaction.fondo_nombre,
        "TipoTransaccion": transaction.tipo_transaccion,
        "Monto": transaction.monto,
        "SaldoRestante": transaction.saldo_restante,
        "Fecha": transaction_date,
        "Notificacion": transaction.notificacion,
    }
    table.put_item(Item=item)
    return


def fund_unsubscribe_db(*, transaction: Transaccion, db):
    table = db.Table("amaris")
    transaction_date = datetime.now().isoformat()

    item = {
        "PK": f"Usuario#1",
        "SK": f"TRANSACCION#{transaction_date}",
        "TipoEntidad": "TRANSACCION",
        "FondoID": transaction.fondo_id,
        "FondoNombre": transaction.fondo_nombre,
        "TipoTransaccion": "cancelacion",
        "Monto": transaction.monto,
        "SaldoRestante": transaction.saldo_restante
        + transaction.monto,  # Se devuelve el monto al saldo restante
        "Fecha": transaction_date,
        "Notificacion": transaction.notificacion,
    }
    table.put_item(Item=item)
    return


def history_db(*, db):
    table = db.Table("amaris")

    response = table.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key("PK").eq(f"Usuario#1")
        & boto3.dynamodb.conditions.Key("SK").begins_with("TRANSACCION#")
    )
    return response


def get_funds_db(*, db):
    table = db.Table("amaris-funds")
    response = table.scan()
    return response["Items"]
