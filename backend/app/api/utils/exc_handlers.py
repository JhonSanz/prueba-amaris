from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.api.schemas.base import std_response
from app.api.utils.exceptions import InsuficientMoney


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    msg = ", ".join([f"{error['loc'][-1]}: {error['msg']}" for error in errors])
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"ok": False, "msg": f"Validation Error: {msg}", "data": errors},
    )

async def general_exception_handler(request: Request, exc: Exception):
    print(exc)
    return std_response(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        ok=False,
        msg="An unexpected error occurred",
        data=None,
    )

async def insuficient_money_exception_handler(request: Request, exc: InsuficientMoney):
    print(exc)
    return std_response(
        status_code=status.HTTP_400_BAD_REQUEST,
        ok=False,
        msg=str(exc),
        data=None,
    )
