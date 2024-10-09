from uuid import uuid4
from datetime import datetime
from app.api.schemas.fund import FundSubscribe
from app.api.schemas.transaction import Transaccion
from decimal import Decimal


def transaction_create_db(*, transaction: Transaccion, db):
    table = db.Table("amaris-transaction")
    transaction_date = datetime.now().isoformat()
    transaction_id = str(uuid4())
    item = {
        "transactionId": transaction_id,
        "userId": transaction.userId,
        "fundId": transaction.fundId,
        "amount": Decimal(transaction.amount),
        "type": transaction.type,
        "timestamp": transaction_date,
    }
    table.put_item(Item=item)
    return
