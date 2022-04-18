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

    @abstractmethod
    def get_teacher_courses(entity_id: int):
        """Get all courses of teacher"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_by_id(entity_id: str):
        """get entity by id"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def delete(entity_id: str):
        """delete entity into db"""

        raise NotImplementedError("Method not implemented")
