from flask import Flask
from src.config import config
from src.domain import api_main
from typing import Any, Dict, Optional


def init_blueprint(app: Flask) -> None:
    app.register_blueprint(api_main)


def create_app(env: str = "dev", settings: Optional[Dict[str, Any]] = None) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config[env])

    init_blueprint(app)
    return app
