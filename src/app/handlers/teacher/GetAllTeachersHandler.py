from typing import Type

from ...interfaces import ITeacherRepository

from src.shared.src.logic import Result


class GetAllTeachersHandler:
    def __init__(self, teacher_repository: Type[ITeacherRepository]) -> None:
        self.__teacher_repository = teacher_repository

    def handle(self) -> Result[list]:

        teachers = self.__teacher_repository.get()

        return Result.ok(teachers)
