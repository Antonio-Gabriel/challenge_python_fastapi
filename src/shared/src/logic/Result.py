from typing import Generic, TypeVar, Union


T = TypeVar("T")
U = TypeVar("U")


class Result(Generic[T]):

    IS_SUCCESS: bool
    ERROR: Union[T, str]

    def __init__(
        self, is_success: bool, error: Union[T, str] = None, value: T = None
    ) -> None:
        if is_success and error:
            raise Exception(
                "InvalidOperation: A result cannot be successful and contain an error"
            )

        if not is_success and not error:
            raise Exception(
                "InvalidOperation: A failing result needs to contain an error message"
            )

        self.IS_SUCCESS = is_success
        self.ERROR = error
        self._value: T = value

    def get_value(self) -> T:
        """Return value error"""

        if not self.IS_SUCCESS:
            raise Exception(
                "Can't get the value of an error result. Use 'errorValue' instead."
            )

        return self._value

    def error_value(self) -> T:
        """Return error message"""

        return self.ERROR

    @classmethod
    def ok(cls, value: Generic[U] = None):
        """Return ok"""
        return Result[U](True, None, value)

    @classmethod
    def fail(cls, error: any):
        """Return fail message"""
        return Result[U](False, error)
