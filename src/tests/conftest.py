import pytest
from src import create_app
from src.database import db as _db


@pytest.fixture(scope="session")
def app():

    app = create_app("test")
    app_context = app.app_context()
    app_context.push()

    yield app

    app_context.pop()


# noinspection PyShadowingNames
@pytest.fixture(scope="session")
def db(app):
    with app.app_context():
        _db.create_all()
        yield _db
        _db.drop_all()


@pytest.fixture(scope="session")
def flask_client(app, db):
    return app.test_client()


# @pytest.fixture(scope="function")
# def session(db: SQLAlchemy, request: SubRequest) -> scoped_session:
#     """
#     Creates a new persistence session for a tests.
#     http://alexmic.net/flask-sqlalchemy-pytest/
#     """
#     connection = db.engine.connect()
#     transaction = connection.begin()

#     options = dict(bind=connection, binds={})
#     session = db.create_scoped_session(options=options)

#     db.session = session

#     def teardown():
#         transaction.rollback()
#         connection.close()
#         session.remove()

#     request.addfinalizer(teardown)

#     return session
