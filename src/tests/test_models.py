from src.database import db
from src.model.models import User, Todos
import pytest
from faker import Faker


def test_is_app_running(app):
    assert app is not None


def test_is_session_work(session):
    fake = Faker()
    user = {"email": fake.email(), "password": "helloWorld"}


@pytest.mark.parametrize("id, name", [(1, "hellp"), (2, "kko")])
def test_is_session_work(session, id, name):
    user = {"id": id, "name": name}
    session.add(User(**user))
    session.commit()

    res = session.query(User).first()
    assert res.id != 0


def test_related_model_should_connect():
    us = User()
    td = Todos()
    us.todos.append(td)
    assert us is not None


def test_custom_model(session):
    User.create(name="custom")
    res = User.get_user(1)
    assert res.id == 1
    assert res.name == "custom"

