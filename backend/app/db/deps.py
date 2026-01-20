from typing import Generator
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
import os
from dotenv import load_dotenv
from app.db.session import SessionLocal

load_dotenv()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme)):
    # Pulling keys inside the function is safer for hot-reloads
    secret = "supersecretkey"
    algo = os.getenv("ALGORITHM", "HS256")
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, secret, algorithms=[algo])
        user_id: str = payload.get("sub")
        user_role: str = payload.get("role")
        
        if user_id is None:
            raise credentials_exception
            
        return {"id": user_id, "role": user_role}
    except JWTError:
        raise credentials_exception

def check_admin_role(current_user: dict = Depends(get_current_user)):
    if current_user.get("role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to access this resource"
        )
    return current_user