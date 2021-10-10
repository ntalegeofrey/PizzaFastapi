from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker
from config.settings import Settings


psqlt = "postgresql://postgres:@localhost:5432/pizzaapi"

# SQLALCHEMY_DATABASE_URL = Settings.DATABASE_URL

engine = create_engine(psqlt)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
