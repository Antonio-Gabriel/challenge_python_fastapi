import re


class Email:
    @staticmethod
    def is_valid(email: str):
        """Verify if the email address is valid"""

        expretion = r"^([a-z0-9\+_\-]+)(\.[a-z0-9\+_\-]+)*@([a-z0-9\-]+\.)+[a-z]{2,6}$"
        return True if re.search(expretion, email) is not None else False
