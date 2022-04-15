from ..entities.props import UserProps
from ..interfaces import IUserRepository

from ..sql import UserModel
from ..config import session_maker


class UserRepository(IUserRepository):
    def save(entity: UserProps):
        """save entity into db"""

        user = UserModel(
            id=entity.id,
            name=entity.name,
            surname=entity.surname,
            email=entity.email,
            password=entity.password,
            city=entity.city,
            user_type=entity.user_type,
            state=entity.state,
        )

        with session_maker() as session:
            session.add(user)
            session.commit()

        return user

    def update(entity: UserProps):
        """update entity into db"""
        with session_maker() as session:
            user = (
                session.query(UserModel)
                .filter(UserModel.id == entity.id)
                .update(
                    {
                        UserModel.name: entity.name,
                        UserModel.email: entity.email,
                        UserModel.surname: entity.surname,
                        UserModel.city: entity.city,
                        UserModel.state: entity.state,
                    }
                )
            )

            session.commit()
        return user

    def get():
        """get all entities"""
        with session_maker() as session:
            user = session.query(UserModel).all()

        return user

    def get_by_id(entity_id: str):
        """get entity by id"""
        with session_maker() as session:
            user = session.query(UserModel).filter(UserModel.id == entity_id).first()

        return user

    def get_by_name(entity_name: str):
        """get entity by name"""
        with session_maker() as session:
            user = (
                session.query(UserModel)
                .filter(UserModel.name.ilike(f"%{entity_name}%"))
                .all()
            )

        return user

    def get_by_state(entity_state: bool):
        """get entity by state"""
        with session_maker() as session:
            user = (
                session.query(UserModel).filter(UserModel.state == entity_state).all()
            )

        return user

    def get_by_email(email: str):
        """get entity email"""
        with session_maker() as session:
            user = session.query(UserModel).filter(UserModel.email == email).first()
            session.commit()

        return user

    def delete(entity_id: str):
        """delete entity into db"""
        with session_maker() as session:
            user = session.query(UserModel).filter(UserModel.id == entity_id).delete()
            session.commit()

        return user
