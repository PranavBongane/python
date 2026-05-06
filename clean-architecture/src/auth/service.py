from datetime import timedelta, datetime, timezone
from typing import Annotated
from uuid import uuid4, UUID
from fastapi import Depends
from passlib.context import CryptContext
from ..database.core import get_db
import jwt
from jwt import PyJWTError
from sqlalchemy.orm import Session
from src.entities.users import User
from . import models
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from ..exceptions import AuthenticationError
import logging
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return bcrypt_context.hash(password)    

def authenticate_user(email:str, password:str, db:Session) -> User:
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.hashed_password):
        logging.warning(f"Failed login attempt for email: {email}")
        raise AuthenticationError("Invalid email or password")
    return user

def create_access_token(email: str, user_id: UUID, expire_delta: timedelta) -> str:
    to_encode = {
        "sub": email, 
        "id": str(user_id),
        "exp": datetime.now(timezone.utc) + expire_delta
        }
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str) -> models.TokenData:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        user_id: str = payload.get("id")
        if email is None or user_id is None:
            raise AuthenticationError("Invalid token")
        return models.TokenData(user_id=user_id)
    except PyJWTError as e:
        logging.error(f"Token verification error: {str(e)}")
        raise AuthenticationError("Invalid token")
    
def register_user(db:Session, register_user_request: models.RegisterUserRequest) ->  None:
    try:
        create_user_model= User(
            id=uuid4(),
            email=register_user_request.email,
            first_name=register_user_request.first_name,
            last_name=register_user_request.last_name,
            hashed_password=get_password_hash(register_user_request.password)
        )
        db.add(create_user_model)
        db.commit()
    except Exception as e:
        logging.error(f"Error occurred while registering user: {str(e)}")
        raise AuthenticationError("Error occurred while registering user")



def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]) -> models.TokenData:
    token_data = verify_token(token)
    return token_data
currentUser = Annotated[models.TokenData, Depends(get_current_user)]

def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Annotated[Session, Depends(get_db)]) -> models.Token:
    user = authenticate_user(form_data.username, form_data.password, db)

    if not user:
        raise AuthenticationError("Incorrect email or password")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        email=user.email, user_id=user.id, expire_delta=access_token_expires
    )
    return models.Token(access_token=access_token, token_type="bearer")