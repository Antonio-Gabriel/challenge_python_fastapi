from datetime import datetime
from enum import Enum
from typing import List
from pydantic import BaseModel


class ContactsModel(BaseModel):
    id: int
    phone: str
    user_id: int

    class Config:
        orm_mode = True


class TeacherModel(BaseModel):
    id: int
    name: str
    email: str
    surname: str
    city: str
    phone: List[ContactsModel]
    user_type: Enum

    class Config:
        orm_mode = True


class TeacherRelationModel(BaseModel):
    id: int
    name: str
    startDate: datetime
    endDate: datetime
    state: bool

    class Config:
        orm_mode = True


class TeacherResponseModel(BaseModel):
    teachers: List[TeacherModel]


class TeacherRelationResponseModel(BaseModel):
    courses: List[TeacherRelationModel]
    total_students: int
