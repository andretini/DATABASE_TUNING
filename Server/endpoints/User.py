from fastapi import APIRouter, HTTPException, Query
from database import get_connection

router = APIRouter(prefix="/users", tags=["Users"])

# Rota para listar todos os usuários
@router.get("/all")
async def read_users():
    connection = get_connection()
    if connection is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return users

# Rota para listar um usuário específico
@router.get("/")
async def read_user(id: int = Query(None)):
    connection = get_connection()
    if connection is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
    user = cursor.fetchone()
    
    cursor.close()
    connection.close()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

# Rota para criar um novo usuário
@router.post("/create")
async def create_user(user: dict):
    connection = get_connection()
    if connection is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    cursor = connection.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, password, email, telefone_usuario) VALUES (%s, %s, %s, %s)",
            (user['username'], user['password'], user['email'], user['phone'])
        )
        connection.commit()
        return {"username": user["username"]}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        connection.close()

# Rota para editar um usuário existente
@router.put("/edit/{id}")
async def update_user(id: int, user: dict):
    connection = get_connection()
    if connection is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    cursor = connection.cursor()
    try:
        cursor.execute(
            "UPDATE users SET username = %s, password = %s, email = %s, telefone_usuario = %s WHERE id = %s",
            (user['username'], user['password'], user['email'], user['phone'], id)
        )
        connection.commit()
        
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="User not found")
        
        return {"message": f"User with ID {id} updated successfully"}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        connection.close()

# Rota para deletar um usuário existente
@router.delete("/delete/{id}")
async def delete_user(id: int):
    connection = get_connection()
    if connection is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM users WHERE id = %s", (id,))
        connection.commit()
        
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="User not found")
        
        return {"message": f"User with ID {id} deleted successfully"}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        connection.close()
