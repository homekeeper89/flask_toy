import requests

from pytest_bdd import parsers, scenarios, given, when, then

scenarios("../features/user.feature", example_converters=dict(phrase=str))


@given('the app api is queried with "<phrase>"')
def app_response(phrase):
    params = {"q": phrase, "format": "json", "code": 200}
    return params


@then(parsers.parse('the response status code is "{code:d}"'))
def response_code(app_response, code):
    assert app_response["code"] == code


@then('the response contains results for "<phrase>"')
def response_contents(app_response, phrase):
    assert phrase.lower() == app_response["q"]

