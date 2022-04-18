from fastapi import APIRouter, status, Depends

from ...adapter import CourseAdapter
from ...config import AuthMiddleware
from ...decorators.Authorization import Authorization
from ...repositories import CourseRepository

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from .schemas.CourseSchema import CourseSchema
from .schemas.CourseResponseModel import CourseResponseModel
from ..user.schemas.UserResponseModel import GenericUserModel

from ...handlers import CreateCourseHandler, GetAllCoursesHandler, GetCoursesByTeacher


course_routes = APIRouter(
    prefix="/api",
    tags=["Course"],
)


@course_routes.get("/courses", response_model=CourseResponseModel)
@Authorization("staff")
async def get(auth=Depends(AuthMiddleware.auth_wrapper)):
    """Get all courses"""
    course_handle = GetAllCoursesHandler(CourseRepository)
    result = course_handle.handle()

    return {"courses": result.get_value()}


@course_routes.get("/courses/teacher/{id}", response_model=CourseResponseModel)
@Authorization("staff", "teacher")
async def get_course_by_teacher(id: int, auth=Depends(AuthMiddleware.auth_wrapper)):
    """Get all courses by teacher"""
    course_handle = GetCoursesByTeacher(CourseRepository)
    result = course_handle.handle(id)

    return {"courses": result.get_value()}


@course_routes.post(
    "/course/create",
    response_model=GenericUserModel,
    response_description="Success Responde",
)
@Authorization("staff")
async def create(course: CourseSchema, auth=Depends(AuthMiddleware.auth_wrapper)):
    """Create course"""

    course_adapter = CourseAdapter.create(
        name=course.name,
        startDate=course.startDate,
        endDate=course.endDate,
        state=course.state,
        teacher_id=course.teacher_id,
    )

    error_entity = course_adapter.error_value()
    if error_entity:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=jsonable_encoder(
                {
                    "detail": {"msg": error_entity},
                }
            ),
        )

    course_handle = CreateCourseHandler(CourseRepository)
    result = course_handle.handle(course_adapter.get_value())

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
                "detail": {"msg": "Successfully course created!"},
            }
        ),
    )
