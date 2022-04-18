from fastapi import APIRouter, status, Depends

from ...adapter import UserAdapter
from ...config import AuthMiddleware
from ...decorators.Authorization import Authorization
from ...repositories import UserRepository, StudentRepository


from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from .schemas.StudentSchema import StudentSchema
from .schemas.StudentResponseModel import StudentResponseModel

from ..course.schemas.CourseResponseModel import CourseResponseModel

from ..user.schemas.AuthSchema import AuthSchema, AuthResponseModel
from ..user.schemas.UserResponseModel import GenericUserModel, UserCreateModels

from ...handlers import (
    AuthUserHandler,
    CreateStudentHandler,
    UpdateUserHandler,
    GetAllStudentsHandler,
    GelStudentCoursesHandler,
)


student_routes = APIRouter(
    prefix="/api",
    tags=["Student"],
)


@student_routes.post("/student/auth", response_model=AuthResponseModel)
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


@student_routes.get("/students", response_model=StudentResponseModel)
@Authorization("staff")
async def get_teachers(auth=Depends(AuthMiddleware.auth_wrapper)):

    students_handler = GetAllStudentsHandler(StudentRepository)
    students = students_handler.handle()
    return {"students": students.get_value()}


@student_routes.get("/student/courses/{id}", response_model=CourseResponseModel)
@Authorization("student")
async def get_teachers(id: int, auth=Depends(AuthMiddleware.auth_wrapper)):

    courses_handler = GelStudentCoursesHandler(StudentRepository)
    coueses = courses_handler.handle(id)
    return {"courses": coueses.get_value()}


@student_routes.post(
    "/student/create",
    response_model=GenericUserModel,
    response_description="Success Responde",
)
@Authorization("staff")
async def create_student(
    user_props: StudentSchema, auth=Depends(AuthMiddleware.auth_wrapper)
):
    """Create user staff"""

    user_result = UserAdapter.create(
        name=user_props.name,
        email=user_props.email,
        surname=user_props.surname,
        password=user_props.password,
        city=user_props.city,
        state=user_props.state,
        user_type="student",
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

    student_handle = CreateStudentHandler(UserRepository, StudentRepository)
    result = student_handle.handle(user_result.get_value(), user_props.contacts)

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
                "detail": {"msg": "Successfully student created!"},
            }
        ),
    )


@student_routes.put(
    "/student/update/{id}",
    response_model=GenericUserModel,
    response_description="Success Responde",
)
@Authorization("student")
async def update(
    id: str, user_props: UserCreateModels, auth=Depends(AuthMiddleware.auth_wrapper)
):
    """Update user student"""

    user_result = UserAdapter.create(
        name=user_props.name,
        email=user_props.email,
        surname=user_props.surname,
        password=user_props.password,
        city=user_props.city,
        state=user_props.state,
        user_type="student",
        id=id,
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

    user_handler = UpdateUserHandler(UserRepository)
    result = user_handler.handle(user_result.get_value())

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
                "detail": {"msg": "Successfully user updated!"},
            }
        ),
    )
