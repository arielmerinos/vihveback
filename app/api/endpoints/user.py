from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.crud import crud_user
from app.schemas import user as user_schema
from app.api.deps import get_db

router = APIRouter()

@router.post("/users/", response_model=user_schema.UserRead)  # Cambiado de UserCreate a UserRead para la respuesta
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, email=user.email)
    print("DEBUG: user", user)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud_user.create_user(db=db, user=user)

# Asegúrate de que la función get_users() esté utilizando el esquema correcto para la respuesta.
@router.get("/users/", response_model=List[user_schema.UserRead])  # Cambiado de User a UserRead
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud_user.get_users(db, skip=skip, limit=limit)
    return users
