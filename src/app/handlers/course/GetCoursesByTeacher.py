from typing import Type

from ...interfaces import ICourseRepository

from src.shared.src.logic import Result


class GetCoursesByTeacher:
    def __init__(self, course_repository: Type[ICourseRepository]) -> None:
        self.__course_repository = course_repository

    def handle(self, teacher_id: int) -> Result[list]:

        courses = self.__course_repository.get_by_teacher_id(teacher_id)

        return Result.ok(courses)
