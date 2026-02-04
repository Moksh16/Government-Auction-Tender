from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from .settings import settings


SQLALCHEMY_database_url = settings.neon_url
engine = create_engine(SQLALCHEMY_database_url)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()