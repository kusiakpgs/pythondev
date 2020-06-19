import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DB_ENDPOINT = os.environ.get('DB_ENDPOINT') or 'error'

    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #                           'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:adminadmin@' + DB_ENDPOINT + ':3306/tkusiakdb'

    SQLALCHEMY_TRACK_MODIFICATIONS = False