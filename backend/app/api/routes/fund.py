# notify


from fastapi import APIRouter, Depends, Query, status
from app.api.schemas.fund import FundSubscribe, FundUnsubscribe
from app.api.schemas.transaction import Transaccion
from app.api.schemas.base import StandardResponse, std_response
from app.database.connection import get_db
from app.api.crud import fund as fund_crud
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/health")
async def health():
    return JSONResponse(status_code=200, content={"status": "healthy"})


@router.get("/list", response_model=StandardResponse)
async def get_funds(
    db=Depends(get_db),
):
    result = fund_crud.get_funds(db=db)
    return std_response(status_code=status.HTTP_200_OK, ok=True, msg="", data=result)


@router.get("/history", response_model=StandardResponse)
async def get_history(
    db=Depends(get_db),
):
    result = fund_crud.history(db=db)
    return std_response(status_code=status.HTTP_200_OK, ok=True, msg="", data=result)


@router.post("/subscribe", response_model=StandardResponse)
async def subscribe(
    transaction: Transaccion,
    db=Depends(get_db),
):
    expense_result = fund_crud.fund_subscribe(db=db, transaction=transaction)
    return std_response(
        status_code=status.HTTP_200_OK, ok=True, msg="", data=expense_result
    )


@router.post("/unsubscribe", response_model=StandardResponse)
async def unsubscribe(
    transaction: Transaccion,
    db=Depends(get_db),
):
    expense_result = fund_crud.fund_unsubscribe(db=db, transaction=transaction)
    return std_response(
        status_code=status.HTTP_200_OK, ok=True, msg="", data=expense_result
    )
