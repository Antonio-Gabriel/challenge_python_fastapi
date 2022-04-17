from enum import Enum
from typing import List
from pydantic import BaseModel


class UserModels(BaseModel):
    id: int
    name: str
    email: str
    surname: str
    city: str
    password: str
    state: bool
    user_type: Enum

    class Config:
        orm_mode = True


class UserCreateModels(BaseModel):
    name: str
    email: str
    surname: str
    city: str
    password: str
    state: bool

    class Config:
        orm_mode = True


class UserResponseModel(BaseModel):
    users: List[UserModels]

    class Config:
        orm_mode = True


class UserByIdResponseModel(BaseModel):
    user: UserModels

    class Config:
        orm_mode = True


class GenericBaseModelProps(BaseModel):
    msg: str


class GenericUserModel(BaseModel):
    detail: GenericBaseModelProps
