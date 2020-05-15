import pytest
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


@pytest.fixture(scope="session")
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
