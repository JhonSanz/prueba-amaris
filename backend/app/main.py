from fastapi import FastAPI, Request, status
from app.api.router import api_router
from fastapi.middleware.cors import CORSMiddleware
from app.api.utils.exc_handlers import (
    validation_exception_handler,
    general_exception_handler,
)
from fastapi.exceptions import RequestValidationError


app = FastAPI()
app.include_router(api_router)


app.add_exception_handler(Exception, general_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

origins = [
    "*",
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
