from typing import List, Tuple
from app.api.schemas.fund import FundSubscribe, FundUnsubscribe
from app.api.schemas.transaction import Transaccion
from app.database.repository.fund import (
    fund_subscribe_db,
    fund_unsubscribe_db,
    history_db,
    get_funds_db,
)
from app.database.repository.transaction import transaction_create_db
from app.database.repository.user import user_update_db, user_get_db
from app.database.repository.fund import get_fund_db
from app.api.utils.exceptions import InsuficientMoney


def fund_subscribe(*, db, transaction: Transaccion):
    fund = get_fund_db(db=db, fund_id=transaction.fundId)
    user = user_get_db(db=db, user_id=transaction.userId)

    if fund["amount"] > user["money"]:
        raise InsuficientMoney(
            f"No tiene saldo disponible para vincularse al fondo {fund['name']}"
        )

    subscriptions = user["subscriptions"]
    new_subscription = {"fundId": transaction.fundId}
    found = False
    for subscription in subscriptions:
        if subscription["fundId"] == new_subscription["fundId"]:
            found = True
            break

    if not found:
        subscriptions.append(new_subscription)

    new_money = user["money"] - fund["amount"]
    data = {":subs": subscriptions, ":new_money": new_money}
    user_update_db(user_id=transaction.userId, data=data, db=db)
    transaction_create_db(transaction=transaction, db=db)
    return


def fund_unsubscribe(*, db, transaction: Transaccion):
    fund = get_fund_db(db=db, fund_id=transaction.fundId)
    user = user_get_db(db=db, user_id=transaction.userId)

    subscriptions = user["subscriptions"]
    subscription_found = None
    for subscription in subscriptions:
        if subscription["fundId"] == transaction.fundId:
            subscription_found = subscription
            break

    if not subscription_found:
        raise Exception(f"El usuario no está suscrito al fondo {fund['name']}")

    subscriptions.remove(subscription_found)
    new_money = user["money"] + fund["amount"]
    data = {":subs": subscriptions, ":new_money": new_money}
    user_update_db(user_id=transaction.userId, data=data, db=db)
    transaction_create_db(transaction=transaction, db=db)
    return


def history(*, db):
    response = history_db(db=db, user_id="user_001")
    if not response:
        raise Exception("No se encontraron transacciones para este usuario.")
    return response


def get_funds(*, db):
    result = get_funds_db(db=db)
    if not result:
        raise Exception("No se encontraron fondos de inversión.")
    return result


def get_client(*, db, client_id: str):
    user = user_get_db(db=db, user_id=client_id)
    return user
