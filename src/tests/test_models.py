from src.database import db
from src.model.models import User
import pytest


def test_is_app_running(app):
    assert app is not None


def test_is_session_work(session):
    user = {"id": 1, "name": "helloWorld"}
    session.add(User(**user))
    session.commit()

    res = session.query(User).first()
    assert res.id != 0
