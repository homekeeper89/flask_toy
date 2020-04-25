from src.domain.todo.repository import TodoRepository
from src.domain.user.repository import UserRepository
from src.model.models import Todos, User
import pytest


@pytest.mark.todo
def test_create_todo_should_success(session):
    user_data = {"name": "test_man"}
    todo_data = {"user_id": 1, "title": "test_title", "contents": "test_contents"}

    data = User(**user_data)
    UserRepository.create(data)

    data = Todos(**todo_data)
    TodoRepository.create(data)

    res = session.query(Todos).first()
    assert res.user_id == todo_data.get("user_id")
