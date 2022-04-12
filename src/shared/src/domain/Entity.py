from abc import ABC
from typing import Generic, TypeVar

T = TypeVar("T")


class Entity(ABC, Generic[T]):
    """Entity base for all domain entities

    Args:
        ABC (_type_): abstract class
        Generic (_type_): generic class
    """

    def __init__(self, props: T, id: str = None):
        self._id = id
        self.props = props

    @property
    def id(self):
        """Return entity id"""

        return self._id
