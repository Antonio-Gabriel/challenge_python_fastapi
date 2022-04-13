from hashlib import blake2b
from hmac import compare_digest


class PasswordHash:

    SECRET_KEY = b"wedev_learning_password_hashSecretKey"
    DIGEST_SIZE = 20

    @classmethod
    def encrypt(cls, password: str) -> bytes:
        """Enctrypt password"""

        if password:
            hash_blake = blake2b(digest_size=cls.DIGEST_SIZE, key=cls.SECRET_KEY)
            hash_blake.update(password.encode())
            return hash_blake.hexdigest().encode("utf8")

    @classmethod
    def compare(cls, current_pass: str, comparison_pass: bytes) -> bool:
        """Check if password is valid"""

        password_generate = cls.encrypt(current_pass)
        if not compare_digest(password_generate, comparison_pass):
            return False

        return True
