import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "super-sEcReat"


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

