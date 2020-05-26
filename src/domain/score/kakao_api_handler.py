import requests

import asyncio
import aiohttp


class KakaoApiHandler:
    KAKAO_HOST = "https://dapi.kakao.com"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {"Authorization": "KakaoAK {}".format(self.api_key)}
        self.values = []
        self._radius = 2000  # 2km

    def set_radius(self, radius: int) -> None:
        self._radius = int(radius)

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

    def get_category_data(self, request: dict) -> dict:
        data = self.parse_request(request)
        for category in data["category_group"]:
            res = self.send_api(category, data)
        return res

    async def get_api(self, category, url):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url) as response:
                self.set_meta_value(category, await response.json())

    def get_category_data_async(self, request):
        parsed_data = self.parse_request(request)
        self.set_radius(parsed_data.get("radius", 2000))
        api_data = self.make_api_url_list(parsed_data)
        tasks = [self.get_api(api["category"], api["url"]) for api in api_data]
        asyncio.run(asyncio.wait(tasks))
        return True

    def set_meta_value(self, category: str, response: dict) -> None:
        value = response["meta"].get("total_count", 0)
        data = {"category": category, "total_count": value}
        self.values.append(data)

    def make_api_url_list(self, parsed_data) -> list:
        url_list = [
            {"category": category, "url": self.make_category_api(category, parsed_data)}
            for category in parsed_data["category_group"]
        ]
        return url_list

    def make_score(self) -> None:
        [value.update(score=(value["total_count"] / self._radius)) for value in self.values]

