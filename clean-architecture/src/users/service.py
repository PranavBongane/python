from uuid import UUID
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from . import models
from src.entities.users import User
from src.exceptions import UserNotFoundError, invalidPasswordError, PasswordsDoNotMatchError
from src.auth.service import verify_password, get_password_hash
import logging

def get_user_by_id(db: Session, user_id: UUID) -> models.UserResponse:
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        logging.error(f"User with id {user_id} not found.")
        raise UserNotFoundError(user_id)
    logging.info(f"User with id {user_id} retrieved successfully.")
    return models.UserResponse(
        id=user.id,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        created_at=user.created_at,
        updated_at=user.updated_at
    )

def change_user_password(db: Session, user_id: UUID, password_change: models.PasswordChange) -> None:
    try:
        user  = get_user_by_id(db, user_id)
        #verify current password
        if not verify_password(password_change.current_password, user.password):
            logging.error(f"Invalid current password for user with id {user_id}.")
            raise invalidPasswordError()
        #check if new passwords match
        if password_change.new_password != password_change.new_password_confirm:
            logging.error(f"New passwords do not match for user with id {user_id}.")
            raise PasswordsDoNotMatchError()
        #update password
        user.password = get_password_hash(password_change.new_password)
        db.add(user)
        db.commit()
        logging.info(f"Password for user with id {user_id} changed successfully.")
    except UserNotFoundError as e:
        logging.error(str(e))
        raise HttpException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except (invalidPasswordError, PasswordsDoNotMatchError) as e:
        logging.error(str(e))
        raise HttpException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) 
    