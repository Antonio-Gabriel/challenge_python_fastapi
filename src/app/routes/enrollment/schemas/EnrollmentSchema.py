from pydantic import BaseModel


class EnrollmentSchema(BaseModel):
    student_id: int
    course_id: int
