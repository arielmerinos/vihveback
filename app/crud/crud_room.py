import app.db.models.room as models
import app.db.base as database
from sqlalchemy.orm import Session
from app.db.models.room import Room
from app.schemas.room import RoomCreate


def create_room(db: Session, room: RoomCreate) -> Room:
    db_room = Room(name=room.name)
    try:
        db.add(db_room)
        db.commit()
        db.refresh(db_room)
    except Exception as e:
        db.rollback()
        raise e
    return db_room

def get_room(db: Session, room_id: str):
    return db.query(Room).filter(Room.name == room_id).first()


