import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    SECRET = os.getenv("SECRET")
    # DATABASE_URL = os.getenv("DATABASE_URL")
    """DATABASE_URL = postgresql://YOUR_DATABASE_USERNAME:YOUR_DATABASE_PASSWORD@localhost:5432/YOUR_DATABASE_NAME')"""
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
    DEBUG = False
    DATABASE_URL = 'admin://xarplzfllomlvr:b52cdb7c12c1d0175f7569876e8ceaae7d36a3387b93b876f58c67839c95b9a2@ec2-107-22-175-33.compute-1.amazonaws.com:5432/d498qmhc8lmfvk'
    


app_config = {
    'DEFAULT': DevelopmentConfiguration,
    'TESTING': TestingConfiguration,
    'DEVELOPMENT': DevelopmentConfiguration,
    'PRODUCTION': ProductionConfiguration
}
