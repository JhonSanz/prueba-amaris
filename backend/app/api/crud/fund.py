from typing import List, Tuple
from app.api.schemas.fund import FundSubscribe, FundUnsubscribe
from app.api.schemas.transaction import Transaccion
from app.database.repository.fund import (
    fund_subscribe_db,
    fund_unsubscribe_db,
    history_db,
    get_funds_db,
)


# el usuario incia con 500000


def fund_subscribe(*, db, transaction: Transaccion):
    # obtener información del fondo para ver el monto mínimo y poder suscribirse
    # if (monto_min_del_fondo > monto_cliente)
    #   raise Exception("No tiene saldo disponible para vincularse al fondo <Nombre delfondo>")
    fund_subscribe_db(transaction=transaction, db=db)
    return


def fund_unsubscribe(*, db, transaction: Transaccion):
    # obtener información del fondo para ver el monto mínimo y devolverlo al cliente

    fund_unsubscribe_db(transaction=transaction)
    return


def history(*, db):
    response = history_db(db=db)
    if "Items" not in response or not response["Items"]:
        raise Exception(
            status_code=404, detail="No se encontraron transacciones para este usuario."
        )
    return


def get_funds(*, db):
    result = get_funds_db(db=db)
    if not result:
        raise Exception(
            status_code=404, detail="No se encontraron transacciones para este usuario."
        )
    return result
