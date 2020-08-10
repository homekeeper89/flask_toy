import pytest


def test_get_main_should_success(flask_client):
    res = flask_client.get("/")
    assert res.status_code == 200
