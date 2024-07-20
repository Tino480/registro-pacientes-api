from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.users.models import UniversityDegree, kinship


class UserBase(BaseModel):
    name: str
    gender: str
    age: int
    date_of_birth: str
    municipality: str
    address: str
    phone: int
    religion: str
    civil_status: str
    university_degree: UniversityDegree
    registration: str
    tutor: str
    emergency_number: int
    kinship: kinship
    diagnostic_print: str


class UserCreate(UserBase, BaseModel):
    pass


class UserUpdate(BaseModel):
    name: str | None = None
    gender: str | None = None
    age: int | None = None
    date_of_birth: str | None = None
    municipality: str | None = None
    address: str | None = None
    phone: int | None = None
    religion: str | None = None
    civil_status: str | None = None
    university_degree: UniversityDegree | None = None
    registration: str | None = None
    tutor: str | None = None
    emergency_number: int | None = None
    kinship: Optional["kinship"] = None
    diagnostic_print: str | None = None


class UserGet(UserBase):
    id: int
    updated_at: datetime
    created_at: datetime

    class Config:
        orm_mode = True
