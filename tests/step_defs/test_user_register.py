from pytest_bdd import scenarios, given, when, then, parsers

scenarios("../features/user_register.feature")


@given(parsers.parse("user give us {user_id}"))
def make_user_id(user_id):
    return make_user_id


@when(parsers.parse("the user_id is same to {limit_word}"))
def compare_word_to_user_id(make_user_id, limit_word):
    return limit_word


@then(parsers.parse("i should return {message} and {code}"))
def make_message(message, code):
    assert True
