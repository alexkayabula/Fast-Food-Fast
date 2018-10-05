import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    SECRET = os.getenv("SECRET")
    # DATABASE_URL = os.getenv("DATABASE_URL")
    DATABASE_URL = 'postgresql://postgres:k0779211758aj@localhost:5432/order_db'


class DevelopmentConfiguration(Config):
    """Configurations for Development."""
    DEBUG = True


class TestingConfiguration(Config):
    """Configurations for Testing."""
    TESTING = True
    DEBUG = True
    DATABASE_URL = 'postgresql://postgres:k0779211758aj@localhost:5432/test_db'


class ProductionConfiguration(Config):
    """Configurations for Production."""
    DEBUG = True
    DATABASE_URL = 'postgres://eyzxekqeckzgjc:78e620ab085ae62514bd49db48ce33ec3c50df764c5822e6d8ec9d7607527534@ec2-23-23-80-20.compute-1.amazonaws.com:5432/dac1le4vb3d4of'


app_config = {
    'DEFAULT':ProductionConfiguration ,
    'TESTING': TestingConfiguration,
    'DEVELOPMENT': DevelopmentConfiguration,
    'PRODUCTION': ProductionConfiguration
}
