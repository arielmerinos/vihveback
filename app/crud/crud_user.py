from sqlalchemy.orm import Session
from typing import List
from ..db.models.user import User
from ..schemas.user import UserCreate
from passlib.context import CryptContext

# Inicializamos passlib con bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    # Hash a password using bcrypt within passlib for consistency
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Check if the provided password matches the stored password (hashed)
    return pwd_context.verify(plain_password, hashed_password)

def get_user_by_email(db: Session, email: str) -> User:
    # Query the database for a user by email
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate) -> User:
    # Create a new user with hashed password
    hashed_password = hash_password(user.password)
    db_user = User(name=user.name, email=user.email, hashed_password=hashed_password)
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        db.rollback()  # Important to rollback the session if there's an error
        raise e
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
    # Retrieve a list of users, with offset and limit for pagination
    return db.query(User).offset(skip).limit(limit).all()