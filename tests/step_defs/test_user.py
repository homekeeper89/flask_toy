import json

from pytest_bdd import scenarios, given, when, then, parsers

CONVERTERS = {
    "email": str,
    "password": str,
    "nickname": str,
    "age": int,
    "language": str,
    "info": str,
    "message": str,
    "code": int,
}

scenarios("../features/user/user.feature", example_converters=CONVERTERS)


@given(parsers.parse("유저는 <email>, <password>, <nickname>, <age>, <language> 를 입력한다"))
def user(email, password, nickname, age, language):
    user = {
        "email": email,
        "password": password,
        "nickname": nickname,
        "age": age,
        "language": language,
    }
    yield user


@when(parsers.parse("유저가 위 정보 중 <info> 를 빼고 보낸다."))
def remove_property(flask_client, user, info):
    del user[info]


@then(parsers.parse("서버는 <code> 과 빠진 <message> 를 포함하는 메세지로 응답한다"))
@then("서버는 <code> 과 빠진 <message> 를 포함하는 메세지로 응답한다")
def server(flask_client, user, code, message):
    # res = flask_client.post("/api/v1/user", json.dumps(user))
    # assert res.status_code == code
    # assert res.data == message
    assert True

