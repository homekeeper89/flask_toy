import pytest
from pytest_bdd import scenarios, given, when, then, parsers

scenarios("../features/user_register.feature")


@given(parsers.parse("user give us {user_id}"))
def make_user_id(user_id):
    return make_user_id


@pytest.fixture  # when 은 자동 fixture로 사용 못하는 듯
@when(parsers.parse("the user_id is same to {limit_word}"))
def compare_word_to_user_id(make_user_id, limit_word):
    return limit_word


@then(parsers.parse("i should return {message} and {code}"))
def make_message(compare_word_to_user_id, make_user_id, message, code):
    assert True
