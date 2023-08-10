import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')
class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_HOST')
    DEBUG=True
    SQLALCHEMY_ECHO=True
