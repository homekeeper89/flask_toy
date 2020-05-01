from src.domain.user import api_user, jsonify
from src.domain.user.usecase import UserUseCase
from flask import request
from flasgger import swag_from


@api_user.route("/", methods=["POST"])
@swag_from("createUser.yml")
def register():
    data = request.json
    res = UserUseCase().register(data)

    res = "success" if res else "fail"
    return jsonify({"data": res})

