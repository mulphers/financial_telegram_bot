from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserDTO(BaseModel):
    user_id: int
    username: str
    is_active: bool
    is_admin: bool
    created_at: datetime
    updated_at: datetime


class UserCreate(BaseModel):
    user_id: int
    username: str
    is_active: Optional[bool] = None
    is_admin: Optional[bool] = None


class UserUpdate(BaseModel):
    username: Optional[str] = None
    is_active: Optional[bool] = None
    is_admin: Optional[bool] = None
