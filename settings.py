import os

API_TOKEN = "INT TOKEN_BOT"

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'data.db')
