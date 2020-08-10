import pytest
import random
import json
from unittest.mock import Mock
from requests.models import Response
from .factory.factories import UserFactory, TodosFactory, UserWithTodoFactory
from src import create_app
from src.database import db as _db

# https://stewartadam.io/blog/2019/04/04/testing-flask-applications-code-database-views-flask-config-and-app-context-pytest


@pytest.fixture(scope="session")
def app():

    app = create_app("test")
    app_context = app.app_context()
    app_context.push()

    yield app

    app_context.pop()


@pytest.fixture(scope="session")
def db(app):
    with app.app_context():
        _db.create_all()
        yield _db
        _db.drop_all()


@pytest.fixture(scope="session")
def flask_client(app, db):
    return app.test_client()


@pytest.fixture(scope="function")
def session(app, db, request):
    """Creates a new database session for each test, rolling back changes afterwards"""
    connection = _db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = _db.create_scoped_session(options=options)

    _db.session = session

    yield session

    transaction.rollback()
    connection.close()
    session.remove()


@pytest.fixture
def make_data_preset(session):
    UserFactory._meta.sqlalchemy_session = session
    TodosFactory._meta.sqlalchemy_session = session
    UserWithTodoFactory._meta.sqlalchemy_session = session
    UserFactory.create_batch(10)


@pytest.fixture
def category_search_request():
    data = {
        "user_id": "some_user_id",
        "some_info": "some_info",
        "data": {
            "category_group": ["MT1", "CS2", "PS3", "SC4"],
            "x": "126.948141",
            "y": "37.370773",
            "radius": 20000,
        },
    }
    return data


@pytest.fixture
def category_search_response():

    rand_num = random.randint(50, 100)
    res = Mock(spec=Response)
    res.json.return_value = {"meta": {"total_count": rand_num}}
    # {"document": {}, "meta": {"total_count": random.randint(50, 100)}}
    return res
