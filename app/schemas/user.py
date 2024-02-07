from pydantic import BaseModel, EmailStr, validator, ValidationError, HttpUrl
from typing import Optional
from datetime import datetime
import re

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    password_confirmation: str
    username: str
    profile_picture: Optional[HttpUrl] = None
    bio: Optional[str] = None
    is_public_profile: Optional[bool] = True
    status: Optional[str] = 'active'
    role: Optional[str] = 'user'
    notification_settings: Optional[str] = None
    language_preference: Optional[str] = 'es'

    @validator('password')
    def password_complexity(cls, v):
        if len(v) < 8:
            raise ValueError('La contraseña debe tener al menos 8 caracteres')
        if not any(char.isdigit() for char in v):
            raise ValueError('La contraseña debe incluir al menos un número')
        if not any(char.isupper() for char in v):
            raise ValueError('La contraseña debe incluir al menos una letra mayúscula')
        if not re.search(r"[!#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', v):
            raise ValueError("La contraseña debe incluir al menos un carácter especial")
        return v

    @validator('password_confirmation')
    def passwords_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('Las contraseñas no coinciden')
        return v


# Esquema para leer la información del usuario
class UserRead(BaseModel):
    id: int
    name: str
    email: EmailStr
    username: Optional[str] = None  # Haciendo este campo opcional
    profile_picture: Optional[HttpUrl] = None  # Haciendo este campo opcional
    bio: Optional[str] = None  # Haciendo este campo opcional
    date_joined: datetime
    last_login: Optional[datetime] = None  # Haciendo este campo opcional
    is_public_profile: bool
    is_online: bool
    status: Optional[str] = None  # Haciendo este campo opcional
    role: Optional[str] = None  # Haciendo este campo opcional
    notification_settings: Optional[str] = None  # Haciendo este campo opcional
    language_preference: str



class UserUpdate(BaseModel):
    # Campos opcionales para la actualización
    name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    profile_picture: Optional[HttpUrl] = None
    bio: Optional[str] = None
    is_public_profile: Optional[bool] = None
    status: Optional[str] = None
    role: Optional[str] = None
    notification_settings: Optional[str] = None
    language_preference: Optional[str] = None