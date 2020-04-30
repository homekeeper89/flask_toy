from flask import Flask
from src.config import config
from src.domain import api_main
from src.domain import api_user
from typing import Any, Dict, Optional
from src.database import db
from src.database import migrate


def init_blueprint(app: Flask) -> None:
    app.register_blueprint(api_main)
    app.register_blueprint(api_user)


def create_app(env: str = "dev") -> Flask:
    app = Flask(__name__)
    app.config.from_object(config[env])
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # warning 뜨는 것
    db.init_app(app)
    init_blueprint(app)
    migrate.init_app(app, db)
    return app
