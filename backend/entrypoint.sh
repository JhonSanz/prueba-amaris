#!/bin/bash

# Ejecutar el script para poblar las tablas de DynamoDB
python seed.py

# Iniciar el servidor FastAPI
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
