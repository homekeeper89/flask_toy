from . import api_main, request, jsonify
from redis import Redis

redis = Redis(host="redis", db=0, socket_timeout=5, charset="utf-8", decode_responses=True)


@api_main.route("/test", methods=["POST", "GET"])
def index():

    if request.method == "POST":
        name = request.json["name"]
        redis.rpush("students", {"name": name})
        return jsonify({"name": name})

    if request.method == "GET":
        return jsonify(redis.lrange("students", 0, -1))


@api_main.route("/")
def main():
    return jsonify("sucess")

