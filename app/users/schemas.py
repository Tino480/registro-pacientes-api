from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.users.models import UniversityDegree, kinship, TypeFamily, Symptom

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


class ConsultationBase(BaseModel):
    user_id: int
    note_two: str
    note_one: str
    type_family: TypeFamily 
    children: bool
    type_medic: str
    accident: str
    symptom: Symptom
    assitance_psychologist: str
    type_psychologist: str


class ConsultationCreate(ConsultationBase, BaseModel):
    pass


class ConsultationUpdate(BaseModel):
    note_two: str | None = None
    note_one: str | None = None
    type_family: TypeFamily | None = None
    children: bool | None = None
    type_medic: str | None = None
    accident: str | None = None
    symptom: Optional["Symptom"] = None
    assitance_psychologist: str | None = None
    type_psychologist: str | None = None
    


class ConsultationGet(ConsultationBase):
    id: int
    update_at: datetime
    created_at: datetime

    class Config:
        orm_mode = True
