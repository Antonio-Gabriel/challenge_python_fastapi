import psycopg2
from datetime import datetime

from .enums.Users import Users

from sqlalchemy import (
    Table,
    Enum,
    Column,
    String,
    Boolean,
    MetaData,
    DateTime,
    ForeignKey,
    TIMESTAMP,
    create_engine,
)

engine = create_engine(
    "postgresql://admin:postgresdb2022@localhost/courseDb", echo=True
)
metadata_object = MetaData(bind=engine)

user = Table(
    "user",
    metadata_object,
    Column("id", String(40), nullable=False, primary_key=True),
    Column("password", String(60), nullable=False),
    Column("name", String(60), nullable=False),
    Column("surname", String(60), nullable=False),
    Column("email", String(60), nullable=False),
    Column("state", Boolean, default=True),
    Column("city", String(45), nullable=False),
    Column("address", String(45), nullable=False),
    Column("type", Enum(Users), default="staff"),
)

teacher = Table(
    "teacher",
    metadata_object,
    Column("id", String(40), nullable=False, primary_key=True),
    Column("user_id", String(40), ForeignKey("user.id")),
    Column("created_at", TIMESTAMP, default=datetime.now),
    Column("updated_at", TIMESTAMP, default=datetime.now, onupdate=datetime.now),
)

student = Table(
    "student",
    metadata_object,
    Column("id", String(40), nullable=False, primary_key=True),
    Column("user_id", String(40), ForeignKey("user.id")),
    Column("created_at", TIMESTAMP, default=datetime.now),
    Column("updated_at", TIMESTAMP, default=datetime.now, onupdate=datetime.now),
)

course = Table(
    "course",
    metadata_object,
    Column("id", String(40), nullable=False, primary_key=True),
    Column("name", String(60), nullable=False),
    Column("startDate", DateTime, nullable=False),
    Column("endDate", DateTime, nullable=False),
    Column("state", Boolean, default=True),
    Column("teacher_id", String(40), ForeignKey("teacher.id")),
    Column("created_at", TIMESTAMP, default=datetime.now),
    Column("updated_at", TIMESTAMP, default=datetime.now, onupdate=datetime.now),
)

enrollment = Table(
    "enrollment",
    metadata_object,
    Column("student_id", String(40), ForeignKey("student.id")),
    Column("course_id", String(40), ForeignKey("course.id")),
    Column("created_at", TIMESTAMP, default=datetime.now),
    Column("updated_at", TIMESTAMP, default=datetime.now, onupdate=datetime.now),
)

contact = Table(
    "contact",
    metadata_object,
    Column("id", String(40), nullable=False, primary_key=True),
    Column("phone", String(40), nullable=False, primary_key=True),
    Column("user_id", String(40), ForeignKey("user.id")),
)


metadata_object.create_all()
