from pydantic import BaseModel, EmailStr

# Esquema para crear un usuario
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

# Esquema para leer la información del usuario
class UserRead(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
