from enum import Enum
from typing import List
from pydantic import BaseModel


class UserModels(BaseModel):
    id: str
    name: str
    email: str
    surname: str
    city: str
    password: str
    state: bool
    user_type: Enum

    class Config:
        orm_mode = True


class UserResponseModel(BaseModel):
    users: List[UserModels]

    class Config:
        orm_mode = True
