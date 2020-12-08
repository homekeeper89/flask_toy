from small_app.connecter import Connecter


def test_auth_connect_should_go_homepage():
    url = "https://soomgo.com/"
    obj = Connecter(url)

    res = obj.execute()
    assert res.status_code == 200
