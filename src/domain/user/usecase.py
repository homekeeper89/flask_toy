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

    @staticmethod
    def get_all(page: int) -> list:

        res = UserRepository.get_all(page)
        data = []
        for _, value in enumerate(res.items):
            data.append(value.to_entity())
        response = {
            "data": data,
            "page": {"page": res.page, "next_page": res.has_next, "total": res.total},
        }
        return response

    @staticmethod
    def delete_user(user_id: int) -> bool:

        res = UserRepository().delete(user_id)

        return res
