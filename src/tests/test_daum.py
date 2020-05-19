from src.domain.score.kakao_api_handler import KakaoApiHandler
import os
import pytest


@pytest.fixture
def api_handler():
    handler = KakaoApiHandler(os.getenv("score_kakao"))
    yield handler


@pytest.fixture
def make_request():
    data = {
        "user_id": "some_user_id",
        "some_info": "some_info",
        "data": {
            "category_group": ["MT1", "CS2", "PS3", "SC4"],
            "x": "126.948141",
            "y": "37.370773",
        },
    }
    return data


def test_parsing_request(api_handler, make_request):
    res = api_handler.parse_request(make_request)
    assert len(res["category_group"]) >= 1


def test_send_request(api_handler, make_request):
    res = api_handler.get_category_data(make_request)
    assert res is not None

