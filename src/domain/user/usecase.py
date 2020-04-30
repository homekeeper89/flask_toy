import re


def validate_user_data(data: dict) -> bool:
    email_pattern = re.compile("^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    res = email_pattern.match(data["user_email"])
    return True if res is not None else False


class UserUseCase:
    @staticmethod
    def register(data: dict) -> str:
        return "success"
