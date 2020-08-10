import re
import pytest
from src.domain.todo.repository import TodoRepository
from src.domain.user.repository import UserRepository
from src.model.models import Todos, User


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


@pytest.mark.todo
def test_parse_message():
    pattern = re.compile(r"\[\d[.]\d+")
    msg = "Threshold Crossed: 1 out of the last 1 datapoints [2.71186440678953 (10/04/20 08:09:00)] was less than the threshold (100.0) (minimum 1 datapoint for OK -> ALARM transition)."
    pattern.search(msg).group().replace("[", "")
