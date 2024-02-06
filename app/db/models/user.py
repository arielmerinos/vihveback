from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base  # Importa la clase base de SQLAlchemy
from datetime import datetime

class User(Base):  # Hereda de la clase Base
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    username = Column(String, unique=True, index=True)
    profile_picture = Column(String)  # URL to the profile picture
    bio = Column(String)
    date_joined = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime)
    is_public_profile = Column(Boolean, default=True)
    is_online = Column(Boolean, default=False)
    status = Column(String)  # e.g., 'active', 'inactive'
    role = Column(String)  # e.g., 'user', 'admin', 'moderator'
    notification_settings = Column(String)  # Esto podría ser un JSON o campos específicos
    language_preference = Column(String, default='en')

        # Relación uno a muchos: un usuario puede tener muchos posts
    # posts = relationship("Post", back_populates="usuario")