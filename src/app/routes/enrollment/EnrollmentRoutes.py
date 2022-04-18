from fastapi import APIRouter, status, Depends

from ...adapter import EnrollmentAdapter
from ...config import AuthMiddleware
from ...decorators.Authorization import Authorization
from ...repositories import EnrollmentRepository


from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from .schemas.EnrollmentSchema import EnrollmentSchema

from ..user.schemas.UserResponseModel import GenericUserModel

from ...handlers import RegisterStudentHandler


enrollment_routes = APIRouter(
    prefix="/api",
    tags=["Enrollment"],
)


@enrollment_routes.post(
    "/student/register/course",
    response_model=GenericUserModel,
    response_description="Success Responde",
)
@Authorization("student")
async def register_student_in_course(
    enrollment_props: EnrollmentSchema, auth=Depends(AuthMiddleware.auth_wrapper)
):
    """Register student in course"""

    registed_result = EnrollmentAdapter.create(
        course_id=enrollment_props.course_id, student_id=enrollment_props.student_id
    )

    error_entity = registed_result.error_value()
    if error_entity:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content=jsonable_encoder(
                {
                    "detail": {"msg": error_entity},
                }
            ),
        )

    register_handle = RegisterStudentHandler(EnrollmentRepository)
    result = register_handle.handle(registed_result.get_value())

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
                "detail": {"msg": "Successfully student register into course!"},
            }
        ),
    )
