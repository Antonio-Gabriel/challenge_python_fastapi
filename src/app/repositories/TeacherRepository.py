import email
from uuid import uuid4
from typing import List
from ..interfaces import ITeacherRepository
from ..entities.props import TeacherProps, ContactProps

from ..config import session_maker
from ..sql import TeacherModel, ContactModel, UserModel


class TeacherRepository(ITeacherRepository):
    def save(entity: TeacherProps):
        """save entity into db"""

        teacher = TeacherModel(
            id=entity.id,
            user_id=entity.user_id,
        )

        with session_maker() as session:
            session.add(teacher)
            session.commit()

        return teacher

    def register_contacts(*entity: List[ContactProps]):
        """save contacts into db"""
        contact_model = []
        for contact in entity[0]:
            contact_model.append(
                ContactModel(id=uuid4(), phone=contact, user_id=entity[1])
            )

        for teacher_contact in contact_model:
            with session_maker() as session:
                session.add(teacher_contact)
                session.commit()

        return teacher_contact

    def get():
        """Get all teachers"""
        with session_maker() as session:
            teachers = (
                session.query(UserModel)
                .join(TeacherModel)
                .join(ContactModel)
                .values(
                    TeacherModel.id,
                    UserModel.name,
                    UserModel.surname,
                    UserModel.email,
                    UserModel.city,
                    ContactModel.user_id,
                    UserModel.user_type,
                )
            )

            resultList = []
            for id, name, surname, email, city, user_id, user_type in teachers:
                teacher_contacts = (
                    session.query(ContactModel)
                    .filter(ContactModel.user_id == user_id)
                    .all()
                )

                resultList.append(
                    {
                        "id": id,
                        "name": name,
                        "surname": surname,
                        "email": email,
                        "city": city,
                        "phone": teacher_contacts,
                        "user_type": user_type,
                    }
                )

        return resultList
