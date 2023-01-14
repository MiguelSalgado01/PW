from flask import Blueprint,request
from flask import redirect, render_template, url_for
from forms import AdminForm
from models import db , Admin,User
from datetime import datetime

homeModule = Blueprint('homeModule', __name__)


@homeModule.route('/homePage', methods=['GET', 'POST'])
def toHomePage():
    get_Users = db.session.query(User).all()
    form = AdminForm()
    return render_template("index.html", title="Login", get_Users = get_Users)



