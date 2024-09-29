import os
import importlib

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector

from endpoints.Authorization import checkToken

# Establish the connection
connection = mysql.connector.connect(
    host="localhost",         # Replace with your host
    user="root",     # Replace with your username
    password="1234", # Replace with your password
    database="tunning"  # Replace with your database name
)
cursor = connection.cursor()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Domínio da sua aplicação React
    allow_credentials=True,  # Permitir envio de cookies
    allow_methods=["*"],
    allow_headers=["*"],
)


def load_endpoints():
    endpoints_dir = "endpoints"
    for filename in os.listdir(endpoints_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"{endpoints_dir}.{filename[:-3]}"
            module = importlib.import_module(module_name)
            # Incluindo o router do módulo carregado
            if hasattr(module, 'router'):
                if "auth" in filename.lower():  # ou use o nome exato do módulo, se preferir
                    app.include_router(module.router)  # Não adiciona dependência
                else:
                    for route in module.router.routes:
                        route.dependencies.append(Depends(checkToken))
                    app.include_router(module.router)

load_endpoints()

@app.get("/")
async def root():
    return {"message": "Hello World"}

