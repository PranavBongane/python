from datetime import datetime,timezone
from uuid import UUID, uuid4
from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models
from src.entities.todo import Todo
from src.auth.models import TokenData
from src.exceptions import TodoCreationError, TodoNotFoundError
import logging

def create_todo(current_user: TokenData, db: Session, todo: models.TodoCreate) ->Todo:
    try:
        new_todo = Todo(**todo.model_dump())
        new_todo.user_id = current_user.get_uuid()
        db.add(new_todo)
        db.commit()
        db.refresh(new_todo)
        logging.info(f"Todo created with ID: {new_todo.id} for user: {current_user.username}")
        return new_todo
    except Exception as e:
        logging.error(f"Error creating todo for user: {current_user.username} - {str(e)}")
        raise TodoCreationError(str(e))
    
def get_todos(current_user: TokenData, db: Session)-> list[models.TodoResponse]:
    try:
        todos = db.query(Todo).filter(Todo.user_id == current_user.get_uuid()).all()
        logging.info(f"Retrieved {len(todos)} todos for user: {current_user.username}")
        return todos
    except Exception as e:
        logging.error(f"Error retrieving todos for user: {current_user.username} - {str(e)}")
        raise TodoNotFoundError(str(e))

def get_todo_by_id(current_user: TokenData, db: Session, todo_id: UUID) -> models.TodoResponse:
    try:
        todo = db.query(Todo).filter(Todo.id == todo_id, Todo.user_id == current_user.get_uuid()).first()
        if not todo:
            logging.warning(f"Todo with ID: {todo_id} not found for user: {current_user.username}")
            raise TodoNotFoundError(f"Todo with ID {todo_id} not found")
        logging.info(f"Retrieved todo with ID: {todo_id} for user: {current_user.username}")
        return todo
    except Exception as e:
        logging.error(f"Error retrieving todo with ID: {todo_id} for user: {current_user.username} - {str(e)}")
        raise TodoNotFoundError(str(e)) 

def complete_todo(current_user: TokenData, db: Session, todo_id: UUID) -> models.TodoResponse:
    try:
        todo = db.query(Todo).filter(Todo.id == todo_id, Todo.user_id == current_user.get_uuid()).first()
        if not todo:
            logging.warning(f"Todo with ID: {todo_id} not found for user: {current_user.username}")
            raise TodoNotFoundError(f"Todo with ID {todo_id} not found")
        todo.is_completed = True
        todo.completed_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(todo)
        logging.info(f"Marked todo with ID: {todo_id} as completed for user: {current_user.username}")
        return todo
    except Exception as e:
        logging.error(f"Error completing todo with ID: {todo_id} for user: {current_user.username} - {str(e)}")
        raise TodoNotFoundError(str(e))

def delete_todo(current_user: TokenData, db: Session, todo_id: UUID) -> None:
    try:
        todo = db.query(Todo).filter(Todo.id == todo_id, Todo.user_id == current_user.get_uuid()).first()
        if not todo:
            logging.warning(f"Todo with ID: {todo_id} not found for user: {current_user.username}")
            raise TodoNotFoundError(f"Todo with ID {todo_id} not found")
        db.delete(todo)
        db.commit()
        logging.info(f"Deleted todo with ID: {todo_id} for user: {current_user.username}")
    except Exception as e:
        logging.error(f"Error deleting todo with ID: {todo_id} for user: {current_user.username} - {str(e)}")
        raise TodoNotFoundError(str(e))
    
def update_todo(current_user: TokenData, db: Session, todo_id: UUID, updated_todo: models.TodoCreate) -> models.TodoResponse:    
    try:
        todo = db.query(Todo).filter(Todo.id == todo_id, Todo.user_id == current_user.get_uuid()).first()
        if not todo:
            logging.warning(f"Todo with ID: {todo_id} not found for user: {current_user.username}")
            raise TodoNotFoundError(f"Todo with ID {todo_id} not found")
        for key, value in updated_todo.model_dump().items():
            setattr(todo, key, value)
        db.commit()
        db.refresh(todo)
        logging.info(f"Updated todo with ID: {todo_id} for user: {current_user.username}")
        return todo
    except Exception as e:
        logging.error(f"Error updating todo with ID: {todo_id} for user: {current_user.username} - {str(e)}")
        raise TodoNotFoundError(str(e))