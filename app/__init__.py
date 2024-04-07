from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config



app = Flask(__name__)
print(app.config)
app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db) 

app.config.from_object(Config)


from app import models
#print what is in SQLALCHEMY_DATABASE_URI
from app import views


