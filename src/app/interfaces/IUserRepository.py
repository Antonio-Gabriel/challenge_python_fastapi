from abc import ABC, abstractmethod

from ..entities.props import UserProps


class IUserRepository(ABC):
    @abstractmethod
    def save(entity: UserProps):
        """save entity into db"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def update(entity: UserProps):
        """update entity into db"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get():
        """get all entities"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_by_id(entity_id: str):
        """get entity by id"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_by_name(entity_name: str):
        """get entity by name"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_by_state(entity_state: bool):
        """get entity by state"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def get_by_email(email: str):
        """get entity by email"""

        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def delete(entity_id: str):
        """delete entity into db"""

        raise NotImplementedError("Method not implemented")
