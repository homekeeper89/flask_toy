import pytest
from faker import Faker
from src.domain.user.usecase import UserUseCase, validate_user_data
from src.model.models import User
from unittest.mock import patch


def test_post_user_should_success(flask_client):
    res = flask_client.post("/api/v1/user/")
    assert res.status_code == 200


@pytest.mark.parametrize(
    "email, password, expected", [("wkd@naver.com", 12345, True), ("wkd", 12345, False)]
)
@patch("src.domain.user.repository.UserRepository.create")
def test_user_usecase_register_should_success(mock_method, email, password, expected):
    mock_method.return_value = True

    data = {"email": email, "password": password}
    res = UserUseCase().register(data)
    assert res == expected


@patch("src.domain.user.repository.UserRepository.create")
def test_user_usecase_register_with_commit_false_should_false(mock_method):
    mock_method.return_value = False
    fake = Faker()

    data = {"email": fake.email(), "password": fake.name()}
    res = UserUseCase().register(data)
    assert res == False


def test_user_usecase_register_with_repo_should_create_user(session):
    fake = Faker()
    data = {"email": fake.email(), "password": fake.name()}

    UserUseCase().register(data)

    res = session.query(User).first()
    assert res.email == data["email"]


@pytest.mark.parametrize("email, expected", [("wkdg@naver.com", True), ("kkk", False)])
def test_validate_user_data(email, expected):
    data = {"email": email}
    res = validate_user_data(data)
    assert res == expected
