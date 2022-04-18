from typing import Type

from ...interfaces import ICourseRepository

from src.shared.src.logic import Result


class GetAllCoursesHandler:
    def __init__(self, course_repository: Type[ICourseRepository]) -> None:
        self.__course_repository = course_repository

    def handle(self) -> Result[list]:

        courses = self.__course_repository.get()

        return Result.ok(courses)
