from enum import Enum
from typing import List
from pydantic import BaseModel


class ContactsModel(BaseModel):
    id: str
    phone: str
    user_id: str

    class Config:
        orm_mode = True


class TeacherModel(BaseModel):
    id: str
    name: str
    email: str
    surname: str
    city: str
    phone: List[ContactsModel]
    user_type: Enum

    class Config:
        orm_mode = True


class TeacherResponseModel(BaseModel):
    teachers: List[TeacherModel]
