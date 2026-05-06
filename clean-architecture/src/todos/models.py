from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field
from src.entities.todo import Priority

class Todo(BaseModel):
    description: str
    due_date: Optional[datetime] = None
    priority: Priority= Priority.Medium

class TodoCreate(Todo):
    pass

class TodoUpdate(BaseModel):
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    priority: Optional[Priority] = None

class TodoResponse(Todo):
    id:UUID
    is_completed: bool = Field(default=False)
    completed_at: Optional[datetime] = None
    model_config = ConfigDict(from_attributes=True)