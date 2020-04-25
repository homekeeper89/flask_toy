from src.database import db


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

