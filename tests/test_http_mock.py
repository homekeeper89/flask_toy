import sure
import httpretty
import requests


@httpretty.activate
def test_simple_api():
    httpretty.register_uri(httpretty.POST, "https://auth.aitrics.com/api/v1/signin", body="ok")
    response = requests.post(
        "https://auth.aitrics.com/api/v1/signin", {"username": "", "password": ""}
    )
    response.text.should.equal("ok")
