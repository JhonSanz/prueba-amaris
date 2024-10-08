from pydantic import BaseModel


class FundSubscribe(BaseModel):
    user_id: str
    fund_id: str
    amount: float
    type_transaction: str  # 'apertura' o 'cancelacion'


class FundUnsubscribe(BaseModel):
    pass
