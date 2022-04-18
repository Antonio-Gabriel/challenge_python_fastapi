from typing import Type

from ...entities.props import CourseProps
from ...interfaces import ICourseRepository

from src.shared.src.logic import Result


class CreateCourseHandler:
    def __init__(self, course_repository: Type[ICourseRepository]) -> None:
        self.__course_repository = course_repository

    def handle(self, requestDTO: CourseProps) -> Result[CourseProps]:

        check_existent_teacher = self.__course_repository.get_by_id(
            requestDTO.teacher_id
        )

        if not check_existent_teacher:
            return Result.fail("Teacher not found!")

        teacher_already_registed = self.__course_repository.get_by_registed_course(
            requestDTO.teacher_id, requestDTO.name
        )

        if teacher_already_registed:
            return Result.fail("Teacher is registered in this course!")

        statement = self.__course_repository.save(requestDTO)

        if statement:
            return Result.ok(CourseProps)
