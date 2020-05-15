from flask import Blueprint, jsonify

api_user = Blueprint("for_user", __name__, url_prefix="/api/v1/user")

from .view import *
