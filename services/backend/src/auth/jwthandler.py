import os
from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.security import OAuth2
from jose import JWTError, jwt
from tortoise.exceptions import DoesNotExist
from src.schemas.token import TokenData
from src.schemas.users import UserOutSchema
from src.database.models import Users

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class OAuth2PasswordBearerWithCookie(OAuth2):
    """
    a class that inherits from OAuth2

    - read the cookie sent from request
    - ensures that the cookie is a bearer token
    """
    def __init__(
            self,
            token_url: str,
            scheme_name: str=None ,
            scopes: dict=None,
            auto_error: bool=True
    ):
        if not scopes:
            scopes = {}
        flows = OAuthFlowsModel(password={"tokenUrl": token_url,
                                            "scopes": scopes})
        super().__init__(flows=flows, scheme_name=scheme_name, auto_error=auto_error)

    async def __call__(self, request):
        authorization: str = request.cookies.get("Authorization")
        scheme, param = get_authorization_scheme_param(authorization)

        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=401,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            else:
                return None

security = OAuth2PasswordBearerWithCookie(token_url="/login")

def create_access_token(data:dict,
                        expires_delta: Optional[timedelta] = None):
    """
    create a jwt token from the username
    :param data:
    :param expires_delta:
    :return:
    """
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15) # default expire time

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


# get current user
async def get_current_user(token: str = Depends(security)):
    """
    decode the token and validate the user
    :param token:
    :return:
    """
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    try:
        user = await UserOutSchema.from_queryset_single(
            Users.get(username=token_data.username)
        )
    except DoesNotExist:
        raise credentials_exception
    return user