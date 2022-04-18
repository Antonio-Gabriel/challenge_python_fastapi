from typing import Type

from ...interfaces import ITeacherRepository

from src.shared.src.logic import Result


class GetAllCoursesOfTeacherHandler:
    def __init__(self, teacher_repository: Type[ITeacherRepository]) -> None:
        self.__teacher_repository = teacher_repository

    def handle(self, teacher_id: int) -> Result[list]:

        teachers = self.__teacher_repository.get_teacher_courses(teacher_id)

        return Result.ok(teachers)
