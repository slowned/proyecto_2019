class Config(object):
    """
    Common configurations
    """

class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True
    SECRET_KEY = 'p9Bv<3Eid9%$i01'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:admin@localhost/grupo8'
    EXPLAIN_TEMPLATE_LOADING = True

class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = True
    EXPLAIN_TEMPLATE_LOADING = True
    SQLALCHEMY_ECHO = True
    SECRET_KEY = 'p9Bv<3Eid9%$i01'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://grupo8:MTFhMWVmMDkxYmE2@127.0.0.1/grupo8'

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
