from typing import Type

from ...interfaces import IUserRepository

from src.shared.src.logic import Result


class GetUsersByIdHandler:
    def __init__(self, user_repository: Type[IUserRepository]) -> None:
        self.__user_repository = user_repository

    def handle(self, user_id: str) -> Result[dict]:

        filtered_user = self.__user_repository.get_by_id(user_id)

        return Result.ok(filtered_user)
