from typing import List
from abc import ABC, abstractmethod

from ..entities.props import TeacherProps, ContactProps


class ITeacherRepository(ABC):
    @abstractmethod
    def save(entity: TeacherProps):
        """save entity into db"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def register_contacts(*entity: List[ContactProps]):
        """save contacts into db"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get():
        """Get all teachers"""

        raise NotImplementedError("Method not implemented")
