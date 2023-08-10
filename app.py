
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from apk.config import Config
from flask import Flask

db=SQLAlchemy()

def create_app(configs):
    app=Flask(__name__)
    app.config.from_object(configs)
    db.init_app(app)
   
    return app

app= create_app(Config)
migrate=Migrate(app,db)

from apk.models import *
from apk.routes import *
if __name__=="__main__":
    app.run(debug=True)