from fastapi import FastAPI
import mysql

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}