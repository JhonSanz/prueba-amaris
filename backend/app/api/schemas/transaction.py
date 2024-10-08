from pydantic import BaseModel


class Transaccion(BaseModel):
    fondo_id: str
    fondo_nombre: str
    tipo_transaccion: str
    monto: float
    saldo_restante: float
    notificacion: str
