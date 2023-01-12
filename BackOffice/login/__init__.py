from flask import Blueprint
from flask import redirect, render_template, url_for
from forms import UserLoginForm

login = Blueprint('login', __name__)

@login.route('/')
def index():
    return render_template("pages-sign-in.html")

