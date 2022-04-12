from abc import ABC, abstractmethod
from typing import Generic, TypeVar

IRequest = TypeVar("IRequest")
IResponse = TypeVar("IResponse")


class IUseCase(ABC, Generic[IRequest, IResponse]):
    """Usecase interface"""

    @abstractmethod
    def execute(request: IRequest) -> IResponse:
        raise NotImplementedError("Method not implemented")
