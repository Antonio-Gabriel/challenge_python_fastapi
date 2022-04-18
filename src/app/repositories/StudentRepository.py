from typing import List
from ..interfaces import IStudentRepository
from ..entities.props import StudentProps, ContactProps

from ..config import session_maker
from ..sql import StudentModel, ContactModel, UserModel


class StudentRepository(IStudentRepository):
    def save(entity: StudentProps):
        """save entity into db"""

        student = StudentModel(
            user_id=entity.user_id,
        )

        with session_maker() as session:
            session.add(student)
            session.commit()

        return student

    def register_contacts(*entity: List[ContactProps]):
        """save contacts into db"""
        contact_model = []
        for contact in entity[0]:
            contact_model.append(ContactModel(phone=contact, user_id=entity[1]))

        for student_contact in contact_model:
            with session_maker() as session:
                session.add(student_contact)
                session.commit()

        return student_contact

    def get():
        """Get all teachers"""
        with session_maker() as session:
            students = (
                session.query(StudentModel)
                .filter(UserModel.user_type == "student")
                .values(
                    UserModel.id,
                    UserModel.name,
                    UserModel.surname,
                    UserModel.email,
                    UserModel.city,
                    UserModel.user_type,
                )
            )

            result_set = set()
            resultList = []
            for student in students:

                if student.name not in result_set:

                    student_contacts = (
                        session.query(ContactModel)
                        .filter(ContactModel.user_id == UserModel.id)
                        .all()
                    )

                    resultList.append(
                        {
                            "id": student.id,
                            "name": student.name,
                            "surname": student.surname,
                            "email": student.email,
                            "city": student.city,
                            "phone": student_contacts,
                            "user_type": student.user_type,
                        }
                    )

                    result_set.add(student.name)

        return resultList

    def get_by_id(entity_id: str):
        """get entity by id"""
        with session_maker() as session:
            student = (
                session.query(UserModel)
                .filter(UserModel.id == entity_id, UserModel.user_type == "student")
                .first()
            )

        return student

    def delete(entity_id: str):
        """delete entity into db"""
        with session_maker() as session:
            student = (
                session.query(ContactModel)
                .filter(ContactModel.user_id == entity_id)
                .delete()
            )

            session.commit()

        return student
