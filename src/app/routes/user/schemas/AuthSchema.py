from pydantic import BaseModel
from .UserResponseModel import UserModels


class AuthSchema(BaseModel):
    email: str
    password: str


class AuthResponseModel(BaseModel):
    access_token: str
    user: UserModels
    token_type: str
