import requests

import asyncio
import aiohttp


class KakaoApiHandler:
    KAKAO_HOST = "https://dapi.kakao.com"
    CATEGORY_SEARCH_API = "/v2/local/search/category.json?category_group_code=PM9&radius=20000"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {"Authorization": "KakaoAK {}".format(self.api_key)}

    def make_category_api(self, code: str, data_info: dict) -> str:
        radius, y_point, x_point = data_info.get("radius"), data_info.get("y"), data_info.get("x")
        return (
            self.KAKAO_HOST
            + "/"
            + f"/v2/local/search/category.json?category_group_code={code}&radius={radius}&x={x_point}&y={y_point}"
        )

    def send_api(self, code, data):

        api_url = self.make_category_api(code, data)

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

    async def get_api(self, url):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url) as response:
                print("<<<", await response.json())
                await response.text()

    def get_category_data_async(self, request):
        data = self.parse_request(request)
        urls = [self.make_category_api(category, data) for category in data["category_group"]]
        tasks = [self.get_api(url) for url in urls]
        asyncio.run(asyncio.wait(tasks))
        return True
