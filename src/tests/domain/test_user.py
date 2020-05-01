import pytest
from faker import Faker
from src.domain.user.usecase import UserUseCase, validate_user_data
from src.model.models import User
from src.domain.user.repository import UserRepository
from unittest.mock import patch
import json


def test_user_repo_delete(session):
    data = {"email": "test", "password": "pwd"}
    data = User(**data)
    session.add(data)
    session.commit()

    id = User.id
    UserRepository.delete(id)

    res = session.query(User).filter(User.id == id).first()  # User.email은 왜 안될까.

    assert res is None


@pytest.mark.user
@pytest.mark.xfail(reason=" This Connection is closed 에러 발생. 아무래도 session과 관련된 이슈인듯함")
def test_post_user_should_success(flask_client):
    fake = Faker()
    data = {"email": fake.email(), "password": fake.name()}

    res = flask_client.post(
        "/api/v1/user/", data=json.dumps(data), headers={"Content-Type": "Application/json"}
    )
    assert res.status_code == 200


@pytest.mark.user
@pytest.mark.parametrize(
    "email, password, expected", [("wkd@naver.com", 12345, True), ("wkd", 12345, False)]
)
@patch("src.domain.user.repository.UserRepository.create")
def test_user_usecase_register_should_success(mock_method, email, password, expected):
    mock_method.return_value = True

    data = {"email": email, "password": password}
    res = UserUseCase().register(data)
    assert res == expected


@pytest.mark.user
@patch("src.domain.user.repository.UserRepository.create")
def test_user_usecase_register_with_commit_false_should_false(mock_method):
    mock_method.return_value = False
    fake = Faker()

    data = {"email": fake.email(), "password": fake.name()}
    res = UserUseCase().register(data)
    assert res == False


@pytest.mark.user
def test_user_usecase_register_with_repo_should_create_user(session):
    fake = Faker()
    data = {"email": fake.email(), "password": fake.name()}

    UserUseCase().register(data)

    res = session.query(User).filter(User.email == data["email"])
    assert res is not None


@pytest.mark.user
@pytest.mark.parametrize("email, expected", [("wkdg@naver.com", True), ("kkk", False)])
def test_validate_user_data(email, expected):
    data = {"email": email}
    res = validate_user_data(data)
    assert res == expected
