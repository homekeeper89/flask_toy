import traceback
import os

from flask import request, url_for, jsonify
from flask_api import FlaskAPI, status, exceptions
from flask_jwt_extended import ( JWTManager, jwt_required, create_access_token, create_refresh_token, get_jwt_identity, jwt_refresh_token_required )

from functools import wraps
import datetime

app = FlaskAPI(__name__)

app.config['JWT_SECRET_KEY'] = 'super-secret'

app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=10)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = datetime.timedelta(days=15)

jwt = JWTManager(app)

def error_decorator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as ex:
            traceback.print_exc()
            return jsonify({'code':500, 'msg':'Internal Error'}), status.HTTP_500_INTERNAL_SERVER_ERROR
        return decorated_function

@app.route('/', methods=['GET'])
def ping():
    return jsonify({'code':200, 'msg':'success'}), status.HTTP_200_OK

@app.route('/block/<last>', methods=['GET'])
@jwt_required
@error_decorator
def get_blocked_sites(last):
    account = extract_account(request)
    return jsonify({'code':200, 'msg':'SUCCESS', 'clean_news':result['clean_news'], 'last':result['last'] }), status.HTTP_200_OK

def extract_account(payload):
    return get_jwt_identity().lower()
