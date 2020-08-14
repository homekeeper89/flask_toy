from src import create_app
import pytest


@pytest.mark.parametrize("env", [("dev"), ("prod"), ("test")])
def test_create_server_on_env(env):
    app = create_app(env)
    assert app.config["NAME"] == env.upper()
