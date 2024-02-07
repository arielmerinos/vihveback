from fastapi import FastAPI
from app.db.session import engine  # Importar 'engine' desde 'db.session'
from app.db.base import Base       # Importar 'Base'
from app.db.models import user, post          # Importar 'models'
from app.api.endpoints import user as user_endpoint
from app.api.endpoints import room as room_endpoint


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(user_endpoint.router)
app.include_router(room_endpoint.router)
