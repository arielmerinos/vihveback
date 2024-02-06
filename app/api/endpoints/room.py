from fastapi import WebSocket, APIRouter, Depends
from typing import Dict, List
from sqlalchemy.orm import Session
import json
from app.schemas import room as room_schema
from fastapi.routing import APIRoute
from app.crud.crud_room import get_room, create_room
from app import crud, db as database
from app.api.deps import get_db


router = APIRouter()


active_connections: Dict[str, List[WebSocket]] = {}

@router.websocket("/messages/{room_id}")
async def websocket_endpoint(room_id:str, websocket: WebSocket, db: Session = Depends(get_db)):
  room = get_room(db, room_id)
  print("the websocket", websocket.client)
  db.close()
  if not room:
      await websocket.close()
      return

  # Add the websocket connection to the active connections for the room
  if room_id not in active_connections:
      active_connections[room_id] = []
  active_connections[room_id].append(websocket)
  print("active_connections", active_connections)

  try:
      await websocket.accept()

      while True:
          # Receive message from the client
          message = await websocket.receive_text()

          # Construct the message data to be sent
          message_data = {
              "room_id": room_id,
              "message": message,
          }
          json_message = json.dumps(message_data)

          # Broadcast the message to all connected websockets in the room
          for connection in active_connections[room_id]:
            if connection != websocket:
              await connection.send_text(json_message)

  except Exception as e:
        print(e)
        print("Error")
        pass

@router.post("/rooms")
def create_room(room: room_schema.RoomCreate, db: Session = Depends(get_db)):
  print("DEBUG: Here we are")
  # db = database.SessionLocal()
  db_room = create_room(db=db, room=room)
  db.close()
  return {"message": f'Room Id: {db_room.name} is created'}

@router.get("/rooms/{room_id}")
def get_rooms(room_id: str, db: Session = Depends(get_db)):
  room = get_room(db, room_id)
  if room:
    return {"id": room.id, "name": room.name}
  return {"message": "Room not found"}