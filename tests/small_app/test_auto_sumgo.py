# TODO 경로 안맞는 이슈
import pytest

# from small_app.sumgo_worker import SumgoWorker


@pytest.mark.skip
def test_auth_connect_should_go_homepage():
    url = "https://soomgo.com/"
    need_words = ["파이썬", "python"]
    ben_words = ["자바", "Java", "C언어", "c언어"]
    obj = SumgoWorker(url, need_words, ben_words, True)

    res = obj.execute()
    assert res.status_code == 200
