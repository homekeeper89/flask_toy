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
            "radius": 20000,
        },
    }
    return data


def test_parsing_request(api_handler, make_request):
    res = api_handler.parse_request(make_request)
    assert len(res["category_group"]) >= 1


@pytest.mark.xfail(reason="자동으로 돌아가는 경우 401이 뜬다. 이상...")
def test_send_request(api_handler, make_request):
    assert os.getenv("score_kakao") == api_handler.api_key
    res = api_handler.get_category_data(make_request)
    assert res.status_code == 200


def test_make_category_api(api_handler, make_request):
    code = make_request["data"]["category_group"][0]
    radius = make_request["data"]["radius"]
    x = make_request["data"]["x"]
    y = make_request["data"]["y"]
    res = api_handler.make_category_api(code, radius, x, y)
    url = f"/v2/local/search/category.json?category_group_code={code}&radius={radius}&x={x}&y={y}"
    assert res == api_handler.KAKAO_HOST + "/" + url


def test_response_parser(api_handler):
    res = api_handler.parse_response()
    assert res is not None
