from src.domain.score.kakao_api_handler import KakaoApiHandler
import os
import pytest
import time


@pytest.fixture
def api_handler():
    handler = KakaoApiHandler(os.getenv("score_kakao"))
    yield handler


def test_parsing_request(api_handler, category_search_request):
    res = api_handler.parse_request(category_search_request)
    assert len(res["category_group"]) >= 1


@pytest.mark.xfail(reason="자동으로 돌아가는 경우 401이 뜬다. 이상...")
def test_send_request(api_handler, category_search_request):
    assert os.getenv("score_kakao") == api_handler.api_key
    res = api_handler.get_category_data(category_search_request)
    assert res.status_code == 200


def test_make_category_api(api_handler, category_search_request):
    code = category_search_request["data"]["category_group"][0]
    radius = category_search_request["data"]["radius"]
    x = category_search_request["data"]["x"]
    y = category_search_request["data"]["y"]
    res = api_handler.make_category_api(code, category_search_request["data"])
    url = f"/v2/local/search/category.json?category_group_code={code}&radius={radius}&x={x}&y={y}"
    assert res == api_handler.KAKAO_HOST + "/" + url


def test_response_parser(api_handler, category_search_response):
    # data 에는 documents, meta 이렇게 있음
    # meta에는 total_count 정도만 쓰면 될듯..
    api_handler.set_meta_value("GM9", category_search_response.json())
    assert len(api_handler.values) == 1
    assert api_handler.values[0]["total_count"] is not None


@pytest.mark.xfail(reason="자동으로 돌리면 실패가 됨")
def test_send_api_time(api_handler, category_search_request):
    # 19.23s 걸리네
    res = api_handler.get_category_data(category_search_request)
    assert res.status_code == 200


def test_async_request(api_handler, category_search_request):
    # 0.14초 실화냐
    res = api_handler.get_category_data_async(category_search_request)
    assert res is True


def test_make_api_url_list(api_handler, category_search_request):
    parsed_data = api_handler.parse_request(category_search_request)
    res = api_handler.make_api_url_list(parsed_data)
    assert isinstance(res, list) == True
    assert len(list(map(lambda x: x["category"], res))) == len(
        category_search_request["data"]["category_group"]
    )


def test_sum_url_list(api_handler, category_search_request):
    api_handler.get_category_data_async(category_search_request)
    api_handler.make_score()
    assert "category" in api_handler.values[0].keys()

