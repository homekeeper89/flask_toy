from flask import Flask, jsonify
from flasgger import Swagger, swag_from

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/<string:target>', methods=["GET"])
@app.route('/geolocate', methods=["POST"])
@swag_from('colors_get.yml',methods=["GET"])
@swag_from('colors_post.yml', methods=["POST"])
def colors(target):

    return jsonify(target)

app.run(debug=True)