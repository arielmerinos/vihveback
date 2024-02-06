from sqlalchemy import Column, Integer, String
from app.db.base import Base  # Importa la clase base de SQLAlchemy

class Room(Base):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)