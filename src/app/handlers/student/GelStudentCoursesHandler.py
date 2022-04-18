from typing import Type

from ...interfaces import IStudentRepository

from src.shared.src.logic import Result


class GelStudentCoursesHandler:
    def __init__(self, student_repository: Type[IStudentRepository]) -> None:
        self.__student_repository = student_repository

    def handle(self, student_id: int) -> Result[list]:

        students = self.__student_repository.get_student_courses(student_id)

        return Result.ok(students)
