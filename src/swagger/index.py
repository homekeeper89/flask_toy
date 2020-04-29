from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route("/")
def index():
    return "HELLO WORLD"

@app.route("/bar")
def bar():
    return "I am bar"

app.run(debug=True)