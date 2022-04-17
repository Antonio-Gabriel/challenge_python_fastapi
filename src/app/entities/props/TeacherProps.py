from datetime import datetime
from dataclasses import dataclass


@dataclass
class TeacherProps:
    user_id: str
    created_at: datetime = None
    updated_at: datetime = None
