from src.model.models import User, Todos


def test_related_model_should_connect():
    us = User()
    td = Todos()
    us.todos.append(td)
    assert us is not None
