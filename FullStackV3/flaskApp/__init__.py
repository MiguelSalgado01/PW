from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/rides.db'
app.config['SECRET_KEY'] ='hardsecretkey'

db = SQLAlchemy(app)
from flaskApp import routes
