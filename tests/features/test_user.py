import requests

from pytest_bdd import parsers, scenarios, given, when, then

scenarios("./user.feature", example_converters=dict(phrase=str))


@given('the app api is queried with "<phrase>"')
def app_response(phrase):
    params = {"q": phrase, "format": "json"}
    return params


@then('the response contains results for "<phrase>"')
def response_contents(app_response, phrase):
    assert phrase.lower() == app_response["q"]


@then(parsers.parse('the response status code is "{code:d}"'))
def response_code(app_response, code):
    assert app_response["q"] == code
