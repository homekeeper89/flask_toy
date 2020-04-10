from flask import Flask
from src.config import config
from src.domain import api_main
from typing import Any, Dict, Optional
from src.database import db


def init_blueprint(app: Flask) -> None:
    app.register_blueprint(api_main)


def create_app(env: str = "dev") -> Flask:
    app = Flask(__name__)
    app.config.from_object(config[env])
    db.init_app(app)
    init_blueprint(app)
    return app
