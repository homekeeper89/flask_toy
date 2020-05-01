import re
from src.domain.user.repository import UserRepository
from src.model.models import User


def validate_user_data(data: dict) -> bool:
    email_pattern = re.compile("^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    res = email_pattern.match(data["email"])
    return True if res is not None else False


class UserUseCase:
    @staticmethod
    def register(data: dict) -> bool:

        if not validate_user_data(data):
            return False

        user = User(**data)
        if not UserRepository.create(user):
            return False

        return True
