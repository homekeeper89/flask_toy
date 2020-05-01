import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "super-sEcReat"
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DEV_DATABASE_URL")
        or "mysql+mysqlconnector://root:root@localhost:3306/local_dev"
    )


class ProductionConfig(Config):
    NAME = "PROD"
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DEV_DATABASE_URL")
        or "mysql+mysqlconnector://root:root@localhost:3306/local_prod"
    )


class DevelopmentConfig(Config):
    NAME = "DEV"
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DEV_DATABASE_URL")
        or "mysql+mysqlconnector://root:root@localhost:3306/local_dev"
    )


class TestingConfig(Config):
    NAME = "TEST"
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DEV_DATABASE_URL")
        or "mysql+mysqlconnector://root:root@localhost:3306/local_test"
    )


config = {"test": TestingConfig, "dev": DevelopmentConfig, "prod": ProductionConfig}

