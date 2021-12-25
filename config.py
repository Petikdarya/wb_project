import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql://trxntssn:zJWzfMOJRShol9kXxiLAqldh0ZSzZ97N@hattie.db.elephantsql.com/trxntssn'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

