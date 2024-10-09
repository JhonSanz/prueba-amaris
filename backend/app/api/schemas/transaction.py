from pydantic import BaseModel


class Transaccion(BaseModel):
    userId: str
    fundId: str
    amount: float
    type: str
