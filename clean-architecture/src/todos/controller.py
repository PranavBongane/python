from fastapi import APIRouter, status
from typing import List
from uuid import UUID
from ..database.core import DB_session
from ..auth.models import TokenData
from . import service, models
from ..auth.service import currentUser
from typing import Annotated
from fastapi import Depends

router = APIRouter(prefix="/todos", tags=["todos"])


CurrentUser = Annotated[TokenData, Depends(currentUser)]


@router.post("/", response_model=models.TodoResponse, status_code=status.HTTP_201_CREATED)
def create_todo(todo: models.TodoCreate, db: DB_session, current_user: CurrentUser):
    return service.create_todo(current_user, db, todo)


@router.get("/", response_model=List[models.TodoResponse])
def get_todos(db: DB_session, current_user: CurrentUser):
    return service.get_todos(current_user, db)


@router.get("/{todo_id}", response_model=models.TodoResponse)
def get_todo_by_id(todo_id: UUID, db: DB_session, current_user: CurrentUser):
    return service.get_todo_by_id(current_user, db, todo_id)


@router.post("/{todo_id}/complete", response_model=models.TodoResponse)
def complete_todo(todo_id: UUID, db: DB_session, current_user: CurrentUser):
    return service.complete_todo(current_user, db, todo_id)


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: UUID, db: DB_session, current_user: CurrentUser):
    service.delete_todo(current_user, db, todo_id)
    return {"detail": "Todo deleted successfully"}


@router.put("/{todo_id}", response_model=models.TodoResponse)
def update_todo(todo_id: UUID, todo_update: models.TodoUpdate, db: DB_session, current_user: CurrentUser):
    return service.update_todo(current_user, db, todo_id, todo_update)