import traceback
import os

from flask import request, url_for, jsonify
from flask_api import FlaskAPI, status, exceptions
from flask_jwt_extended import ( JWTManager, jwt_required, create_access_token, create_refresh_token, get_jwt_identity, jwt_refresh_token_required )

from functools import wraps
import datetime
import requests
import asyncio
import aiohttp


app = FlaskAPI(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret'

app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=10)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = datetime.timedelta(days=15)

jwt = JWTManager(app)

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
        data = request.json()
        data = data["data"]
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



def error_decorator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as ex:
            traceback.print_exc()
            return jsonify({'code':500, 'msg':'Internal Error'}), status.HTTP_500_INTERNAL_SERVER_ERROR
        return decorated_function

@app.route('/', methods=['GET'])
def ping():
    return jsonify({'code':200, 'msg':'success'}), status.HTTP_200_OK

@app.route("/api/v1/score", methods=['POST'])
def kakao_api(category_search_request):
    handler = KakaoApiHandler(os.getenv("score_kakao", "c478e9ae026d774a5b5268a115e1e379"))
    res = handler.get_category_data_async(category_search_request)
    return jsonify({'code':200, 'msg':'daum'}), status.HTTP_200_OK
