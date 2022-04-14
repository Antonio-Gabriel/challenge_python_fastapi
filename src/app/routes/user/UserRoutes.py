from fastapi import APIRouter

from ...handlers import GetAllUserHandlers
from ...repositories import UserRepository

from .responses.UserResponseModel import UserResponseModel

user_routes = APIRouter(
    prefix="/api",
    tags=["Users"],
)


@user_routes.get("/", response_model=UserResponseModel)
async def get():
    """Get all users"""
    user_handler = GetAllUserHandlers(UserRepository)
    result = user_handler.handle()

    return {"users": result.get_value()}
