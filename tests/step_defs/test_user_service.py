from pytest_bdd import scenarios, given, when, then, parsers

CONVERTERS = {"code": int}
scenarios("../features/user_service.feature", example_converters=CONVERTERS)


@given(parsers.parse("user has type and <unique_key> and <pwd>"))
def user_info(unique_key, pwd):
    return {"id": unique_key, "pwd": pwd}


@when("user want to register")
def register(user_info):
    user_info["res"] = True


@then(parsers.parse("server send to {code:d} and <flag>"))
@then("server send to <code> and <flag>")
def return_code(user_info, code, flag):
    assert code == 200
