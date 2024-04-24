"""Flask Configuration variables."""

from flask_sqlalchemy import SQLAlchemy
from os import environ, path

basedir = path.abspath(path.dirname(__file__))
#TODO is the below important?
#load_dotenv(path.join(basedir, '.env'))

class Config:
    """Set Flask configuration from .env file"""
    #General config
    SECRET_KEY = 'lydia'
    FLASK_APP = 'flask_blog.app'
    SQALCHEMY_DATABASE_URI = 'mysql+pymysql://lydia:celeste@localhost/co2'
    SQALCHEMY_ECHO = False
    SQALCHEMY_TRACK_MODIFICATIONS = False