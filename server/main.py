from flask import Flask, request, jsonify
from redis import Redis
from application.app import api_main

app = Flask(__name__)
app.register_blueprint(api_main)

