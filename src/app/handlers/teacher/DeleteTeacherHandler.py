from typing import Type

from ...interfaces import ITeacherRepository, IUserRepository

from src.shared.src.logic import Result


class DeleteTeacherHandler:
    def __init__(
        self,
        user_repository: Type[IUserRepository],
        teacher_repository: Type[ITeacherRepository],
    ) -> None:
        self.__user_repository = user_repository
        self.__teacher_repository = teacher_repository

    def handle(self, teacher_id: str) -> Result[str]:

        filtered = self.__teacher_repository.get_by_id(teacher_id)

        if not filtered:
            return Result.fail("Teacher not found")

        statement = self.__teacher_repository.delete(teacher_id)

        if statement:
            self.__user_repository.delete(teacher_id)

            return Result.ok("Succefully teacher deleted!")
