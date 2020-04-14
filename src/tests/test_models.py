from src.database import db
from src.model.models import User
import pytest


def test_run_app(app):
    assert app is not None


@pytest.mark.skip(reason="작업중")
def test_db_set(session):
    user = {"nickname": "nickanme", "birthday": "nickanme"}
    session.add(User(**user))
    session.commit()

    res = session.query(User).first()
    assert res.id != 0
