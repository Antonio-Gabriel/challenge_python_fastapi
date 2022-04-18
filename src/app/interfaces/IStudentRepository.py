from typing import List
from abc import ABC, abstractmethod

from ..entities.props import StudentProps, ContactProps


class IStudentRepository(ABC):
    @abstractmethod
    def save(entity: StudentProps):
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
    def get_student_courses(entity_id: str):
        """get stunde courses"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_by_id(entity_id: str):
        """get entity by id"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def delete(entity_id: str):
        """delete entity into db"""

        raise NotImplementedError("Method not implemented")
