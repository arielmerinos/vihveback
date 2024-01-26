from fastapi import FastAPI
from db.session import engine  # Importar 'engine' desde 'db.session'
from db.base import Base       # Importar 'Base'
from db import models          # Importar 'models'
from api.endpoints import user as user_endpoint

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(user_endpoint.router)
