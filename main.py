from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return 'HELLO_WORLD'

app.run(debug=True)