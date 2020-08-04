from src.database import db
from src.model.models import User, Todos
import pytest
from faker import Faker


@pytest.mark.parametrize("name", [("hellp"), ("kko")])
def test_is_session_work(session, name):
    user = {"name": name}
    User.create(**user)
    res = User.get_user_by_name(name)
    assert res is not None


def test_related_model_should_connect():
    us = User()
    td = Todos()
    us.todos.append(td)
    assert us is not None


def test_custom_model(session):
    name = "custom"
    User.create(name=name)
    res = User.get_user_by_name(name)
    # res = User.get_user(1)
    assert res.id == 1
    assert res.name == name


def test_model_hybrid_property(session):
    User.create(name="hybrid", age=10)
    res = User.get_user_by_name("hybrid")
    assert res.diff_age < 0


def test_model_hybrid_function(session):
    User.create(name="hybrid_function", age=10)
    assert True
