from jose import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from datetime import datetime, timedelta


class AuthMiddleware:
    SECUTIRY = HTTPBearer()
    SECRET_KEY = "2ac54d23023bb75036faef061332256818562fdf7599b5d8044d74bbe8719ec9"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    @classmethod
    def encode_token(cls, user: str):
        """Encode token"""
        payload = {
            "exp": datetime.utcnow()
            + timedelta(days=0, minutes=cls.ACCESS_TOKEN_EXPIRE_MINUTES),
            "iat": datetime.utcnow(),
            "sub": user,
        }

        return jwt.encode(payload, cls.SECRET_KEY, algorithm=cls.ALGORITHM)

    @classmethod
    def decode_token(cls, token):
        """Decode json"""
        try:
            payload = jwt.decode(token, cls.SECRET_KEY, algorithms=[cls.ALGORITHM])
            return payload["sub"]
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=401,
                detail="Signature has expired",
                headers={"WWW-Authenticate": "Bearer"},
            )

        except jwt.InvalidTokenError as e:
            raise HTTPException(
                status_code=401,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )

    @classmethod
    def auth_wrapper(cls, auth: HTTPAuthorizationCredentials = Security(SECUTIRY)):
        """Generate Wrapper for authentication"""
        return cls.decode_token(auth.credentials)
