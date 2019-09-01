import os

class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = os.getenv('shadman')
    #SQLALCHEMY_DATABASE_URI = "jdbc:postgresql://192.168.4.176:5432/postgres"

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    #SQLALCHEMY_DATABASE_URI = "jdbc:postgresql://192.168.4.176:5432/postgres"
    JWT_SECRET_KEY = os.getenv('shadman')



app_config = {
    'development': Development,
    'production': Production,
}