import pytest
from pytest_factoryboy import register
from src.model.models import User, Todos
from .factory.factories import UserFactory, TodosFactory, UserWithTodoFactory


# @pytest.mark.skip(reason="skip")
def test_factory_multi(make_data_preset, session):
    user = UserWithTodoFactory.create()
    assert user is not None
    assert len(user.todos) > 0

    user = UserWithTodoFactory.create(todos=3)
    assert len(user.todos) == 3


def test_factory_fixture(make_data_preset, session):
    user = session.query(User).all()
    assert len(user) != 0
