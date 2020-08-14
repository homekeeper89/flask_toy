from src.database import db
from src.model.models import User


class UserRepository:
    def __init__(self):
        pass

    @staticmethod
    def create(data: dict) -> bool:
        db.session.add(data)
        try:
            db.session.commit()
        except Exception as e:
            raise e
        return True

    @staticmethod
    def delete(user_id: int) -> bool:

        try:
            db.session.query(User).filter(User.id == user_id).delete()
        except Exception as e:
            raise e

        return True

    @staticmethod
    def get_all(page: int) -> list:
        try:
            res = db.session.query(User).order_by(User.id.desc()).paginate(page, 10)

        except Exception as e:
            raise e
        return res
