from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from tortoise.contrib.fastapi import HTTPNotFoundError

import src.crud.users as crud
from src.auth.users import validate_user
from src.schemas.token import Status
from src.schemas.users import UserOutSchema, UserInSchema

from src.auth.jwthandler import (
    create_access_token,
    OAuth2PasswordBearerWithCookie,
    get_current_user,
)

router = APIRouter()

@router.post("/register", response_model=UserOutSchema)
async def register_user(user: UserInSchema):
    """
    register a new user
    :param user:
    :return:
    """
    try:
        return await crud.create_user(user)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )

@router.post("login")
async def login(user: OAuth2PasswordRequestForm = Depends()):
    user = await validate_user(user)

    if not user:
        raise HTTPException(status_code=400,
                            detail="Incorrect username or password",
                            headers={"WWW-Authenticate": "Bearer"})

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires
    )
    token = jsonable_encoder(access_token)
    content = {"message": "Login successful"}
    response = JSONResponse(content=content)

    response.set_cookie(
        "Authorization",
        value=f"Bearer {token}",
        httponly=True, # prevent javascript from reading the cookie and sending it to other servers(prevent CSRF)
        max_age=3600,
        expires=3600,
        samesite="lax",
        secure=False
    )

    return response

@router.get("/user/whoami",
            response_model=UserOutSchema
            , dependencies=[Depends(get_current_user)])
async def read_users_me(current_user: UserOutSchema = Depends(get_current_user)):
    return current_user

@router.delete("/user/{user_id}",
               response_model=Status,
               responses={404: {"model": HTTPNotFoundError}},
               dependencies=[Depends(get_current_user)])

async def delete_user(user_id: int):
    """
    delete a user
    :param user_id:
    :return:
    """
    try:
        return await crud.delete_user(user_id)
    except DoesNotExist:

        raise HTTPNotFoundError("User not found")
