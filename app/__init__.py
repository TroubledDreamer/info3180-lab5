from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from flask_wtf.csrf import CSRFProtect 




app = Flask(__name__)
app.config.from_object(Config)

print(app.config['SECRET_KEY'], "dddddddddd")

csrf = CSRFProtect(app)

db = SQLAlchemy(app)

migrate = Migrate(app, db) 

app.config.from_object(Config)

#print the SECRET_KEY




#print what is in SQLALCHEMY_DATABASE_URI
from app import views


