from typing import Optional
from pydantic import BaseModel

# to ensure that the token is string
class TokenData(BaseModel):
    username: Optional[str] = None

# to send status message to the end user
class Status(BaseModel):
    status: str