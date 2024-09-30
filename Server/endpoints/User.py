from fastapi import APIRouter, HTTPException, Query
from database import get_connection

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/all")
async def read_users():
    connection = get_connection()
    if connection is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")  # Supondo que você tenha uma tabela chamada 'users'
    users = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return users

@router.get("/")
async def read_users(id: int = Query(None)):
    connection = get_connection()
    if connection is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    cursor = connection.cursor(dictionary=True)
    dbQuery = f"SELECT * FROM users where id = {id}"
    cursor.execute(dbQuery)  # Supondo que você tenha uma tabela chamada 'users'
    users = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return users


@router.post("/")
async def create_user(user: dict):
    connection = get_connection()
    if connection is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    cursor = connection.cursor()
    try:
        print(user)
        cursor.execute(
            "INSERT INTO users (username, password, email, telefone_usuario) VALUES (%s, %s, %s, %s)",
            (user['username'], user['password'], user['email'], user['phone'])  # Certifique-se de que a chave está correta
        )
        connection.commit()
        return {"username": user["username"]}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        connection.close()

@router.post("/delete/{id}")
async def delete_user(id: int):
    connection = get_connection()
    if connection is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    cursor = connection.cursor()
    try:
        cursor.execute(
            f"DELETE FROM users WHERE id = {id}"
        )
        connection.commit()
        return {"message": "User deleted"}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        connection.close()

