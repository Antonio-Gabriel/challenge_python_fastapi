from typing import Type

from ...interfaces import IUserRepository

from src.shared.src.logic import Result


class DeleteUserHandler:
    def __init__(self, user_repository: Type[IUserRepository]) -> None:
        self.__user_repository = user_repository

    def handle(self, user_id: str) -> Result[str]:

        statement = self.__user_repository.delete(user_id)

        if statement:
            return Result.ok("Succefully user deleted!")
