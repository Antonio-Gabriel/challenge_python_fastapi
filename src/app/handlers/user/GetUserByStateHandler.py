from typing import Type

from ...interfaces import IUserRepository

from src.shared.src.logic import Result


class GetUserByStateHandler:
    def __init__(self, user_repository: Type[IUserRepository]) -> None:
        self.__user_repository = user_repository

    def handle(self, user_state: bool) -> Result[dict]:

        filtered_user = self.__user_repository.get_by_state(user_state)

        return Result.ok(filtered_user)
