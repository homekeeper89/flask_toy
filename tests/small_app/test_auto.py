from small_app.connecter import Connecter


def test_auth_connect_should_go_homepage():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    obj = Connecter(url)

    res = obj.get()
    assert res.status_code == 200
