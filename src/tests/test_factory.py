import pytest
from pytest_factoryboy import register

from .factory.factories import UserFactory, TodosFactory

register(UserFactory)
register(TodosFactory)


@pytest.fixture
def user(user_factory):
    return user_factory()


@pytest.fixture()
def todo(user, todos_factory):

    return todos_factory(user=user)


def test_factory_first(todo):
    import ipdb

    ipdb.set_trace()
    assert todo is not None
    assert todo.user.email is not None
