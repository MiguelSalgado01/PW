from flask import Blueprint,request
from flask import redirect, render_template, url_for
from forms import AdminForm
from models import db , Admin,User
from datetime import datetime

userModule = Blueprint('userModule', __name__)


@userModule.route('/usersPage', methods=['GET', 'POST'])
def toUsersPage():
    get_Users = db.session.query(User).all()
    form = AdminForm()
    return render_template("users.html", title="Login", get_Users = get_Users)



