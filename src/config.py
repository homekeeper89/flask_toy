import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "super-sEcReat"
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DEV_DATABASE_URL")
        or "mysql+mysqlconnector://root:root@my_sql:5678/local_dev"
    )


class ProductionConfig(Config):
    NAME = "PROD"
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DEV_DATABASE_URL")
        or "mysql+mysqlconnector://root:root@my_sql:5678/local_prod"
    )


class DevelopmentConfig(Config):
    NAME = "DEV"
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DEV_DATABASE_URL")
        or "mysql+mysqlconnector://root:root@my_sql:5678/local_prod"
    )


class TestingConfig(Config):
    NAME = "TEST"
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DEV_DATABASE_URL")
        or "mysql+mysqlconnector://root:root@my_sql:5678/local_test"
    )
    KAKAO_API_KEY = "b53870ce18f5edf1a99e3eae379e0abe"


config = {"test": TestingConfig, "dev": DevelopmentConfig, "prod": ProductionConfig}
