from .user import api_user, jsonify


@api_user.route("/", methods=["GET", "PSOT"])
def register():
    return jsonify("success")

