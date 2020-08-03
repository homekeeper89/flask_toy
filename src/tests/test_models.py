from src.database import db
from src.model.models import User, Todos
import pytest
from faker import Faker


def test_is_app_running(app):
    assert app is not None


@pytest.mark.parametrize("id, name", [(1, "hellp"), (2, "kko")])
def test_is_session_work(session, id, name):
    user = {"id": id, "name": name}
    User.create(**user)
    res = User.get_user(id)
    assert res is not None


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

