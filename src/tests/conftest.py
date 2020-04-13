import os
import pytest

from src import create_app
from src.database import db as _db
from alembic.command import upgrade as alembic_upgrade
from alembic.config import Config as AlembicConfig
from alembic.config import Config


TESTDB = "test_project.db"
TESTDB_PATH = "/opt/project/data/{}".format(TESTDB)
TEST_DATABASE_URI = "sqlite:///" + TESTDB_PATH


@pytest.fixture(scope="session")
def app(request):
    """Session-wide test `Flask` application."""
    app = create_app("test")

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope="function")
def flask_client(app):
    return app.test_client()


from alembic.command import upgrade
from alembic.config import Config


@pytest.fixture(scope="session")
def db(app, request):
    """Session-wide test database."""
    if os.path.exists(TESTDB_PATH):
        os.unlink(TESTDB_PATH)

    # def teardown():
    #     _db.drop_all()
    # os.unlink(TESTDB_PATH)

    alembic_config = AlembicConfig("../alembic.ini")
    alembic_config.set_main_option(
        "sqlalchemy.url", "mysql+mysqlconnector://root:root@localhost:3306/flask_test"
    )
    alembic_upgrade(alembic_config, "head")

    # _db.app = app
    # _db.create_all()

    # request.addfinalizer(teardown)
    return _db


from src.model.models import UserModel


@pytest.fixture(scope="function")
def session(db, request):
    """Creates a new database session for a test."""
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session
