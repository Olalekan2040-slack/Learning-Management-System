from pydantic import BaseModel
from typing import Optional

# User model
class User(BaseModel):
    username: str
    email: str
    disabled: Optional[bool] = None
