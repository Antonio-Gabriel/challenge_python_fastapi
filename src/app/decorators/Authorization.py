from functools import wraps
from fastapi import HTTPException


def Authorization(*permitions):
    """Recive authorizations params"""

    def inner(func):
        """Agregate func scoped"""

        @wraps(func)
        async def wrapper(*args, **kwargs):
            """Recive a func parameters"""

            if kwargs["auth"] not in permitions:
                raise HTTPException(
                    status_code=401,
                    detail="Unauthorized access",
                    headers={"WWW-Authenticate": "Bearer"},
                )

            return await func(*args, **kwargs)

        return wrapper

    return inner
