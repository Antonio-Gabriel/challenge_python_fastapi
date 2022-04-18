from enum import Enum
from typing import List
from pydantic import BaseModel


class ContactsModel(BaseModel):
    id: int
    phone: str
    user_id: int

    class Config:
        orm_mode = True


class StudentModel(BaseModel):
    id: int
    name: str
    email: str
    surname: str
    city: str
    phone: List[ContactsModel]
    user_type: Enum

    class Config:
        orm_mode = True


class StudentResponseModel(BaseModel):
    students: List[StudentModel]
