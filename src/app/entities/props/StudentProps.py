from datetime import datetime
from dataclasses import dataclass


@dataclass
class StudentProps:
    user_id: str
    created_at: datetime
    updated_at: datetime
