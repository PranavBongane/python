from fastapi import APIRouter, status
from uuid import UUID
from ..database.core import DB_session
from . import service, models
from ..auth.service import currentUser

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", response_model=models.UserResponse)
def get_current_user(current_user:currentUser, db:DB_session):
    return service.get_user_by_id(db, current_user.id)

@router.put("/change-password", status_code=status.HTTP_200_OK)
def change_password(password_change: models.PasswordChange, current_user:currentUser, db:DB_session):
    service.change_user_password(db, current_user.id, password_change)
    return {"message": "Password changed successfully"}
