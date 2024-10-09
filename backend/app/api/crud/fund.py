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


# el usuario incia con 500000


def fund_subscribe(*, db, transaction: Transaccion):
    fund = get_fund_db(db=db, fund_id=transaction.fundId)
    user = user_get_db(db=db, user_id=transaction.userId)
    print(fund)
    # if (monto_min_del_fondo > monto_cliente)
    #   raise Exception("No tiene saldo disponible para vincularse al fondo <Nombre delfondo>")
    subscriptions = user["subscriptions"]
    new_subscription = {"fundId": transaction.fundId}
    found = False
    for subscription in subscriptions:
        if subscription["fundId"] == new_subscription["fundId"]:
            found = True
            break

    if not found:
        subscriptions.append(new_subscription)

    data = {":subs": subscriptions}
    user_update_db(user_id=transaction.userId, data=data, db=db)
    transaction_create_db(transaction=transaction, db=db)
    return


def fund_unsubscribe(*, db, transaction: Transaccion):
    # obtener información del fondo para ver el monto mínimo y devolverlo al cliente

    fund_unsubscribe_db(transaction=transaction)
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
