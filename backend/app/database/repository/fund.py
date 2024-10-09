from uuid import uuid4
from datetime import datetime
from app.api.schemas.fund import FundSubscribe
from app.api.schemas.transaction import Transaccion
import boto3
from boto3.dynamodb.conditions import Key, Attr


def fund_subscribe_db(*, transaction: Transaccion, db):
    return


def fund_unsubscribe_db(*, transaction: Transaccion, db):
    return


def history_db(*, db, user_id: str):
    table = db.Table("amaris-transaction")

    response = table.scan()
    transactions = response["Items"]
    return transactions


def get_funds_db(*, db):
    table = db.Table("amaris-fund")
    response = table.scan()
    return response["Items"]


def get_fund_db(*, db, fund_id: str):
    table = db.Table("amaris-fund")
    response = table.get_item(Key={"fundId": fund_id})
    return response["Item"]
