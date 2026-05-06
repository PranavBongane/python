from fastapi import FastAPI
from .database.core import Base, engine
from .entities.todo import Todo # Import model to register them
from .entities.users import User # Import model to register them
from .api import register_routes
from .logging import LogLevels, configure_logging

configure_logging(LogLevels.INFO)

app = FastAPI()

""" 
only uncomment below to create new table,
otherwise the test wil fail if not connected
"""
Base.metadata.create_all(bind=engine)

register_routes(app)