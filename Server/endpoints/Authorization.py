from fastapi import FastAPI, APIRouter, HTTPException, Request, Response
import jwt
from datetime import datetime, timedelta
from database import get_connection

router = APIRouter(prefix="/auth", tags=["Auth"])

SECRET_KEY = "top_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@router.post("/login")
async def login(response: Response, user: dict):
    
    username = user.get("username")
    requestPassword = user.get("password")

    connection = get_connection()
    if connection is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()  # Obtenha apenas uma linha
    
    cursor.close()
    connection.close()
    
    db_password = result['password']
    
    print(username)
    print(requestPassword)
    print(db_password)
    
    if requestPassword != db_password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": username}, expires_delta=access_token_expires)
    
    response.set_cookie(key="access_token", value=access_token, httponly=True, secure=True)
    return {"message": "Logged in"}

@router.get("/checkToken")
async def checkToken(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Token not found")
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        # Continue sua lógica com o usuário autenticado
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

    return {"message": f"{username}"}