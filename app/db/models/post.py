from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base  # Importa la clase base de SQLAlchemy
from datetime import datetime

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    author_id = Column(Integer, ForeignKey('users.id'))
    date_created = Column(DateTime, default=datetime.utcnow)
    date_updated = Column(DateTime, default=datetime.utcnow)
    is_published = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    tags = Column(String)  # Esto podría ser un JSON o campos específicos
    language = Column(String, default='es')

    # Relación muchos a uno: un post pertenece a un usuario
    user = relationship("User", back_populates="posts")
# Path: app/db/models/user.py