from pytest_bdd import scenario, given, when, then


@scenario("../features/user_login.feature", "정상 가입 후 로그인 케이스")
def test_user_normal():
    pass


@given("한 User가 있다.")
def user():
    return {"user": ""}


@when("해당 User가 올바른 정보로 가입한다.")
def register(user):
    info = {"username": "salgu", "password": "1234"}
    user["data"] = info
    user["is_login"] = True


@then("정상적으로 로그인이 성공해야 한다.")
def login_success(user):
    assert user["is_login"] == True

