import os

basedir = os.path.abspath(os.path.dirname(__file__))
DB_BACKEND = 'sqlalchemy'


class DevelopmentMixIn(object):
    DEBUG = True


class SQLAlchemyConfig(DevelopmentMixIn):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')


config = {
    'sqlalchemy': SQLAlchemyConfig,
}


def get_config():
    return config[DB_BACKEND]
