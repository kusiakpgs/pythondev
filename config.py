import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #                           'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:adminadmin@tkusiak-db-tf-pro.cn10audml9ef.eu-west-1.rds.amazonaws.com:3306/tkusiakdb'

    SQLALCHEMY_TRACK_MODIFICATIONS = False