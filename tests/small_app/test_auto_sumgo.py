from small_app.connecter import Connecter


def test_auth_connect_should_go_homepage():
    url = "https://soomgo.com/"
    need_words = ["파이썬", "python"]
    ben_words = ["자바", "Java", "C언어", "c언어"]
    obj = Connecter(url, need_words)

    res = obj.execute()
    assert res.status_code == 200
