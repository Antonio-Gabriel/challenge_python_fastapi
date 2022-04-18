from typing import Type

from ...interfaces import IStudentRepository

from src.shared.src.logic import Result


class GetAllStudentsHandler:
    def __init__(self, student_repository: Type[IStudentRepository]) -> None:
        self.__student_repository = student_repository

    def handle(self) -> Result[list]:

        students = self.__student_repository.get()

        return Result.ok(students)
