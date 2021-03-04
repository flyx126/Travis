class Config(object):
    DEBUG=False
    TESTING=False
    

class DevelopmentConfig(Config):
    DEBUG=True
    PATH_CONFIG = './config/Dashboard_dev.yaml'
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True

class TestingConfig(Config):
    TESTING=True