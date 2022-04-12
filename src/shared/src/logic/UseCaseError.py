from abc import ABC
from dataclasses import dataclass


@dataclass
class IUseCaseErrorError:
    message: str


class UseCaseError(ABC, IUseCaseErrorError):
    def __init__(self, error: IUseCaseErrorError):
        self.message = error.message
