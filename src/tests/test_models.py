from src.database import db
from src.model.models import UserModel


def test_run_app(app):
    assert app is not None


def test_db_set(session):
    user = {"nickname": "nickanme", "birthday": "nickanme"}
    session.add(UserModel(**user))
    session.commit()
    assert UserModel.id > 0
