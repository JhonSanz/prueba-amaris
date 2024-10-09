from uuid import uuid4
from datetime import datetime
from app.api.schemas.fund import FundSubscribe
from app.api.schemas.transaction import Transaccion


def user_get_db(*, db, user_id: int):
    table = db.Table("amaris-users")
    response = table.get_item(Key={"userId": user_id})
    user = response["Item"]
    return user


def user_update_db(*, db, user_id: int, data):
    table = db.Table("amaris-users")
    table.update_item(
        Key={"userId": user_id},
        UpdateExpression="SET subscriptions = :subs, money = :new_money",
        ExpressionAttributeValues={**data},
    )
    return
