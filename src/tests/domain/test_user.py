import pytest
from faker import Faker
from src.domain.user.usecase import UserUseCase, validate_user_data


def test_post_user_should_success(flask_client):
    res = flask_client.post("/api/v1/user/")
    assert res.status_code == 200


def test_user_usecase_register_should_success():
    res = UserUseCase().register({"kk": "kk"})
    assert res == "success"


@pytest.mark.parametrize("email, expected", [("wkdg@naver.com", True), ("kkk", False)])
def test_validate_user_data(email, expected):
    data = {"user_email": email}
    res = validate_user_data(data)
    assert res == expected
