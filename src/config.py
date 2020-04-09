import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "super-sEcReat"
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DEV_DATABASE_URL")
        or "mysql+mysqlconnector://root:root@localhost:3306/flask"
    )


class ProductionConfig(Config):
    DEBUG = False
    NAME = "PROD"


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    NAME = "DEV"


class TestingConfig(Config):
    TESTING = True
    NAME = "TEST"


config = {"test": TestingConfig, "dev": DevelopmentConfig, "prod": ProductionConfig}

