import requests


class KakaoApiHandler:
    KAKAO_HOST = "https://dapi.kakao.com"
    CATEGORY_SEARCH_API = "/v2/local/search/category.json?category\_group\_code=PM9&radius=20000"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def category_search(self):
        api_url = f"{self.KAKAO_HOST}{self.CATEGORY_SEARCH_API}"
        headers = {"Authorization": f"KaKaoAK {self.api_key}"}
        res = requests.get(api_url, headers=headers)
        return res

