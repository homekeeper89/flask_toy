from src.domain.user import api_user, jsonify


@api_user.route("/", methods=["POST"])
def register():
    return jsonify("success")

