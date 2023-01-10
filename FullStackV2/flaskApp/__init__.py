from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskApp import routes

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/rides.db'
app.config['SECRET_KEY'] ='hardsecretkey'

db = SQLAlchemy(app)
db.init_app(app)

