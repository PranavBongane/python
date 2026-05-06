from typing import Annotated
from fastapi import APIRouter, Depends, Request
from starlette import status
from . import models, service
from fastapi.security import OAuth2PasswordRequestForm
from ..database.core import DB_session
from ..rate_limiting import limiter
from..logging import configure_logging

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/", status_code=status.HTTP_201_CREATED)
@limiter.limit("5/minute")
async def register_user(request: Request,
                        db: DB_session, 
                        register_user_request: models.RegisterUserRequest):
    service.register_user(db, register_user_request)


@router.post("/token", response_model=models.Token)
async def login_for_access_token(form_data:Annotated[OAuth2PasswordRequestForm, Depends()], db: DB_session) :
    return service.login_for_access_token(form_data, db)