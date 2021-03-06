from dataclasses import dataclass
from ...sql.enums.Users import Users


@dataclass
class UserProps:
    name: str
    email: str
    surname: str
    city: str
    password: str
    user_type: Users
    state: bool = None
