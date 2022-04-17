from fastapi import APIRouter, status, Depends

from ...config import AuthMiddleware
from ...decorators.Authorization import Authorization
from ...repositories import UserRepository, TeacherRepository


from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


teacher_routes = APIRouter(
    prefix="/api",
    tags=["Teacher"],
)


# @teacher_routes.get("/teachers")
# async def get_teachers():

#     return {"message": "Hello"}
