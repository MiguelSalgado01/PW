from flask import Blueprint
from flask import redirect, render_template, url_for
from forms import UserLoginForm

modulo1 = Blueprint('modulo1', __name__)

@modulo1.route('/')
def index():
   return redirect('/registar')

@modulo1.route('/login', methods=['GET', 'POST'])
def doLogin():
    return render_template("logIn.html")