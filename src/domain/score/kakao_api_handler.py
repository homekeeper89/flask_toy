import requests


class KakaoApiHandler:
    KAKAO_HOST = "https://dapi.kakao.com"
    CATEGORY_SEARCH_API = "/v2/local/search/category.json?category_group_code=PM9&radius=20000"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def make_category_api(self, code: str, radius: int, x_point: str, y_point: str) -> str:
        return (
            self.KAKAO_HOST
            + "/"
            + f"/v2/local/search/category.json?category_group_code={code}&radius={radius}&x={x_point}&y={y_point}"
        )

    def send_api(self, code, data):
        radius, y, x = data.get("radius"), data.get("y"), data.get("x")
        api_url = self.make_category_api(code, radius, x, y)

        kwargs = dict(
            method="get", url=api_url, headers={"Authorization": "KakaoAK {}".format(self.api_key)},
        )

        resp = requests.request(**kwargs)
        return resp

    def parse_request(self, request: dict) -> dict:
        data = request["data"]
        return data

    def parse_response(self, response):
        data = response.json()
        return data

    def get_category_data(self, request: dict) -> dict:
        data = self.parse_request(request)
        for category in data["category_group"]:
            res = self.send_api(category, data)
        return res
