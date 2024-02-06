from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://ariel_dev:pedal9journal8putrid!SCULPTOR@host.docker.internal/vihvelibre_db"
SQLALCHEMY_DATABASE_URL = "postgresql://ariel_dev:pedal9journal8putrid!SCULPTOR@localhost/vihvelibre_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
