from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from typing import List


class UserBase(BaseModel):
    email: EmailStr
    username: str


class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    email: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None



class UserGet(UserBase):
    id: int
    updated_at: datetime
    created_at: datetime


    class Config:
        orm_mode = True
