from datetime import timedelta

class BaseConfig(object):
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    FLASK_ENV = "development"
    FLASK_APP = "app.py"
    FLASK_DEBUG = 0
    SECRET_KEY = "secret_key"
    PERMANENT_SESSION_LIFETIME = timedelta(hours=3)
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_HTTPONLY = False
    REMEMBER_COOKIE_HTTP_ONLY = False
    SESSION_COOKIE_PATH = None

    

class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    FLASK_ENV = "production"
    FLASK_APP = "run.py"
    SECRET_KEY = "secret_key"
    PERMANENT_SESSION_LIFETIME = timedelta(hours=3)
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTP_ONLY = True
    


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True