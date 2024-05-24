"""Flask Configuration variables."""

from flask_sqlalchemy import SQLAlchemy
from os import environ, path
import mysql.connector


basedir = path.abspath(path.dirname(__file__))
#load_dotenv(path.join(basedir, '.env'))

class Config:
    """Set Flask configuration from .env file"""
    #General config
    SECRET_KEY = 'lydia'
    FLASK_APP = 'flask_blog.app'
    SQALCHEMY_DATABASE_URI = 'mysql+pymysql://lydia:celeste@localhost/flask_co2'
    SQALCHEMY_ECHO = False
    SQALCHEMY_TRACK_MODIFICATIONS = False

mydb = mysql.connector.connect(
    host='localhost',
    user='lydia',
    passwd='celeste',
)

my_cursor = mydb.cursor()

my_cursor.execute('SHOW DATABASES')
for db in my_cursor:
    print(db)
#TODO insert name of database here:
my_cursor.execute('USE ???')

#TODO I don't want sqlite3. Decide what to do instead
#import sqlite3
#import pymysql

#connection = sqlite3.connect('../database.db')


# with open('schema.sql') as f:
#     connection.executescript(f.read())
#
# cur = connection.cursor()
#my_cursor.execute("INSERT INTO blogposts (title, content) VALUES (%s, %s)",
            # ('First Post', 'Content for the first post')

mydb.commit()
# connection.commit()
# connection.close()