from sqlalchemy import Column, Integer, String
from db.base import Base  # Importa la clase base de SQLAlchemy

class User(Base):  # Hereda de la clase Base
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
