from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
import os
from dotenv import load_dotenv

load_dotenv()

"""you can add a Database URL in .env file like below,"""
DATABASE_URL = os.getenv("DATABASE_URL") 


""" or hard code SQLite here """
#DATABASE_URL = "sqlite:///./todosapp.db"

"""or hard code PostgreSQL here"""
# DATABASE_URL = "postgresql://postgres:Pass123@localhost:5432/todosapp"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

DB_session = Annotated[Session, Depends(get_db)]
