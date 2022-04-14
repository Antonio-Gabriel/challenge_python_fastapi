from datetime import datetime
from dataclasses import dataclass


@dataclass
class CourseProps:
    name: str
    startDate: datetime
    endDate: datetime
    state: bool
    teacher_id: str
    created_at: datetime
    updated_at: datetime
