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
