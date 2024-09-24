from fastapi import FastAPI
import mysql.connector

# Establish the connection
connection = mysql.connector.connect(
    host="localhost",         # Replace with your host
    user="root",     # Replace with your username
    password="1234", # Replace with your password
    database="tunning"  # Replace with your database name
)

cursor = connection.cursor()


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/usuarios")
async def getUsuarios():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

