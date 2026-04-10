from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

dburl = "postgresql://postgres:Pass123@localhost:5432/demo"
engine = create_engine(dburl)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)