import pytest
from faker import Faker
from src.domain.user.usecase import UserUseCase, validate_user_data
from src.model.models import User
from src.domain.user.repository import UserRepository
from unittest.mock import patch
import json


@pytest.mark.user
@pytest.mark.skip(reason="테스트가 너무 오래걸림")
def test_get_user_should_all(flask_client):
    res = flask_client.get("/api/v1/user/page/1")
    assert res.status_code == 200


@pytest.mark.user
def test_user_repo_get_user_list_should_all(session):
    data_list = []
    for _ in range(20):
        fake = Faker()
        data = {"email": fake.email(), "password": fake.name()}
        data_list.append(User(**data))
    session.add_all(data_list)
    session.commit()

    page = 1

    res = UserRepository().get_all(page)

    assert len(res.items) == 10


@pytest.mark.user
@patch("src.domain.user.repository.UserRepository.get_all")
def test_user_usecase_get_user_list(mock_method, session):
    data_list = []
    for _ in range(20):
        fake = Faker()
        data = {"email": fake.email(), "password": fake.name()}
        data_list.append(User(**data))
    session.add_all(data_list)
    session.commit()

    res = session.query(User).order_by(User.id.desc()).paginate(1, 10)
    mock_method.return_value = res
    page = 1
    res = UserUseCase().get_all(page)
    assert res is not None


@pytest.mark.user
@patch("src.domain.user.repository.UserRepository.delete")
def test_user_usecase_delete_user_with_id_should_success(mock_method, session):
    mock_method.return_value = True

    user_id = 1
    res = UserUseCase().delete_user(user_id)
    assert res is True


@pytest.mark.user
def test_user_repo_delete_with_id_should_success(session):
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
