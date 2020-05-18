import requests


class KakaoApiHandler:
    KAKAO_HOST = "https://dapi.kakao.com"
    CATEGORY_SEARCH_API = "/v2/local/search/category.json?category_group_code=PM9&radius=20000"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def category_search(self):
        y, x = "37.370773", "126.948141"
        api_url = f"{self.KAKAO_HOST}{self.CATEGORY_SEARCH_API}&x={x}&y={y}"
        kwargs = dict(
            method="get", url=api_url, headers={"Authorization": "KakaoAK {}".format(self.api_key)},
        )
        resp = requests.request(**kwargs)
        return resp

