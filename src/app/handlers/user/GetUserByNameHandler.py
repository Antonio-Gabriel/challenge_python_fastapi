from typing import Type

from ...interfaces import IUserRepository

from src.shared.src.logic import Result


class GetUserByNameHandler:
    def __init__(self, user_repository: Type[IUserRepository]) -> None:
        self.__user_repository = user_repository

    def handle(self, user_name: str) -> Result[dict]:

        filtered_user = self.__user_repository.get_by_name(user_name)

        return Result.ok(filtered_user)
