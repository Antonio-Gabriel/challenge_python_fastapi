from typing import Type

from ...entities.props import EnrollmentProps
from ...interfaces import IEnrollmentRepository

from src.shared.src.logic import Result


class RegisterStudentHandler:
    def __init__(self, enrollment_repository: Type[IEnrollmentRepository]) -> None:
        self.__enrollment_repository = enrollment_repository

    def handle(self, requestDTO: EnrollmentProps) -> Result[EnrollmentProps]:

        student_already_registered = (
            self.__enrollment_repository.get_registered_student(
                course_id=requestDTO.course_id, student_id=requestDTO.student_id
            )
        )

        if student_already_registered:
            return Result.fail("The student is already registered in this course!")

        statement = self.__enrollment_repository.register(requestDTO)

        if statement:
            return Result.ok(EnrollmentProps)
