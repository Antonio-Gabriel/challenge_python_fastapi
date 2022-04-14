from dataclasses import dataclass
from src.shared.src.logic import Result, UseCaseError


@dataclass
class IUseCaseErrorError:
    message: str


class EmailAlreadyExists(Result[UseCaseError]):
    def __init__(self, email: str) -> None:
        super().__init__(
            False,
            IUseCaseErrorError(message=f"The email {email} already exist"),
        )
