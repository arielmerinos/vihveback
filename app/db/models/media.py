from base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


# Suponiendo una estructura simple para medios, podría ser una tabla aparte o gestionada de otra forma dependiendo de los requisitos
class Media(Base):
    __tablename__ = "medias"
    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    type = Column(String)
    url = Column(String)

    post = relationship("Post", back_populates="medias")