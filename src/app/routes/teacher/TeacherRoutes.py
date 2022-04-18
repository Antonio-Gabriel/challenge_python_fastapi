from fastapi import APIRouter, status, Depends

from ...adapter import UserAdapter
from ...config import AuthMiddleware
from ...decorators.Authorization import Authorization
from ...repositories import UserRepository, TeacherRepository


from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from .schemas.TeacherSchema import TeacherSchema
from .schemas.TeacherResponseModel import (
    TeacherResponseModel,
    TeacherRelationResponseModel,
)

from ..user.schemas.UserResponseModel import GenericUserModel
from ..user.schemas.AuthSchema import AuthSchema, AuthResponseModel

from ...handlers import (
    AuthUserHandler,
    CreateTeacherHandler,
    GetAllTeachersHandler,
    GetAllCoursesOfTeacherHandler,
    DeleteTeacherHandler,
)


teacher_routes = APIRouter(
    prefix="/api",
    tags=["Teacher"],
)


@teacher_routes.post("/teacher/auth", response_model=AuthResponseModel)
async def auth(credentials: AuthSchema):
    """Authenticate user"""

    auth_handle = AuthUserHandler(UserRepository)
    response = auth_handle.handle(
        email=credentials.email, password=credentials.password
    )
    error = response.error_value()

    if error:
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content=jsonable_encoder(
                {
                    "detail": error,
                }
            ),
        )

    return {
        "access_token": AuthMiddleware.encode_token(
            response.get_value().user_type.value
        ),
        "token_type": "Bearer",
        "user": response.get_value(),
    }


@teacher_routes.get("/teachers", response_model=TeacherResponseModel)
@Authorization("staff")
async def get_teachers(auth=Depends(AuthMiddleware.auth_wrapper)):

    teacher_handle = GetAllTeachersHandler(TeacherRepository)
    teachers = teacher_handle.handle()

    return {"teachers": teachers.get_value()}


@teacher_routes.get(
    "/teacher/courses/{id}", response_model=TeacherRelationResponseModel
)
@Authorization("teacher")
async def get_all_courses_of_teacher(
    id: int, auth=Depends(AuthMiddleware.auth_wrapper)
):

    teacher_handle = GetAllCoursesOfTeacherHandler(TeacherRepository)
    teachers = teacher_handle.handle(id)

    return {
        "courses": teachers.get_value()["courses"],
        "total_students": teachers.get_value()["total_students"],
    }


@teacher_routes.post(
    "/teacher/create",
    response_model=GenericUserModel,
    response_description="Success Responde",
)
@Authorization("staff")
async def create_teacher(
    user_props: TeacherSchema, auth=Depends(AuthMiddleware.auth_wrapper)
):
    """Create user staff"""

    user_result = UserAdapter.create(
        name=user_props.name,
        email=user_props.email,
        surname=user_props.surname,
        password=user_props.password,
        city=user_props.city,
        state=user_props.state,
        user_type="teacher",
    )

    error_entity = user_result.error_value()
    if error_entity:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=jsonable_encoder(
                {
                    "detail": {"msg": error_entity},
                }
            ),
        )

    teacher_handler = CreateTeacherHandler(UserRepository, TeacherRepository)
    result = teacher_handler.handle(user_result.get_value(), user_props.contacts)

    error = result.error_value()

    if error:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=jsonable_encoder(
                {
                    "detail": {"msg": error},
                }
            ),
        )

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder(
            {
                "detail": {"msg": "Successfully teacher created!"},
            }
        ),
    )
