from src.domain.score.kakao_api_handler import KakaoApiHandler
import os

KAKAO_API_KEY = "b53870ce18f5edf1a99e3eae379e0abe"


def test_get_os_env():
    res = os.getenv("score_kakao", False)
    assert res == False


def test_send_api():
    ka = KakaoApiHandler(KAKAO_API_KEY)
    res = ka.category_search()
    assert res.status == 200
