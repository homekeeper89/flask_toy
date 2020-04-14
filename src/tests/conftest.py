import pytest
from src import create_app


@pytest.fixture(scope="session")
def app():

    app = create_app("testing")
    app_context = app.app_context()
    app_context.push()

    yield app

    app_context.pop()


@pytest.fixture(scope="session")
def flask_client(app):
    return app.test_client()
