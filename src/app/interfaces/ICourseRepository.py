from typing import List
from abc import ABC, abstractmethod

from ..entities.props import CourseProps


class ICourseRepository(ABC):
    @abstractmethod
    def save(entity: CourseProps):
        """save entity into db"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get():
        """Get all courses"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_by_id(entity_id: str, course_name: str):
        """get entity by id"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_by_teacher_id(entity_id: str):
        """get entity by id"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_by_registed_course(entity_id: str, course_name: str):
        """get entity by id"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def update(entity: CourseProps):
        """update entity into db"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def delete(entity_id: str):
        """delete entity into db"""

        raise NotImplementedError("Method not implemented")
