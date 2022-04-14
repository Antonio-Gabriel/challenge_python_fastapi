from datetime import datetime
from dataclasses import dataclass


@dataclass
class EnrollmentProps:
    student_id: str
    course_id: str
    created_at: datetime
    updated_at: datetime
