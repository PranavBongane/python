from fastapi import FastAPI
from src.todos.controller import router as todos_router
from src.users.controller import router as users_router
from src.auth.controller import router as auth_router


def register_routes(app: FastAPI):
    app.include_router(todos_router, prefix="/todos", tags=["todos"])
    app.include_router(users_router, prefix="/users", tags=["users"])
    app.include_router(auth_router, prefix="/auth", tags=["auth"])
