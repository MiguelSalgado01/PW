from flask import Blueprint,request
from flask import redirect, render_template, url_for
from forms import AdminForm
from models import db , Admin,User
from datetime import datetime

index = Blueprint('index', __name__)


@index.route('/index', methods=['GET', 'POST'])

def toIndex():
    # Query para Buscar all users
    get_Users = db.session.query(User).all()
    form = AdminForm()
       
    
    return render_template("index.html", title="Login", formFront=form)



