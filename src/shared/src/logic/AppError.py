from Result import Result
from dataclasses import dataclass
from UseCaseError import UseCaseError


@dataclass
class IUnexpectedErrorError:
    message: str
    error: any


class UnexpectedError(Result[UseCaseError]):
    def __init__(self, error: any) -> None:
        super().__init__(
            False,
            IUnexpectedErrorError(message="An unexpected error occurred.", error=error),
        )

    @staticmethod
    def create(error: any):
        """Create a custom error"""
        return UnexpectedError(error)
