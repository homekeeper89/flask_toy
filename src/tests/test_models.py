from src.database import db
from src.model.models import User
import pytest


def test_run_app(app):
    assert app is not None


def test_db_set(session):
    user = {"id": 1, "name": "helloWorld"}
    session.add(User(**user))
    session.commit()

    res = session.query(User).first()
    assert res.id != 0
