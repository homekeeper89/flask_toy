from flask import Flask, jsonify
from flasgger import Swagger, swag_from
from swagger import spec

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/<string:target>', methods=["GET"])
@swag_from(spec.specs_dict, methods=["POST"])
def colors(target):

    return jsonify(target)

app.run(debug=True)