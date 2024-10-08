from fastapi import APIRouter
from app.api.routes import fund


api_router = APIRouter()

api_router.include_router(fund.router, prefix="/fund", tags=["fund"])
