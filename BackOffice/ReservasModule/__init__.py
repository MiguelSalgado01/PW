from flask import Blueprint,request
from flask import redirect, render_template, url_for
from forms import AdminForm
from models import db , Admin, User, bcrypt
from flask_login import login_user, logout_user, current_user
from datetime import datetime

login_module = Blueprint('login', __name__)

@login_module.route('/')
def index():
    return redirect('/pages-sign-in')


from flask import Blueprint,request
from flask import redirect, render_template, url_for
from forms import AdminForm
from models import db , Admin,Ride
from datetime import datetime
from flask_login import current_user

reservasModule = Blueprint('reservasModule', __name__)

@reservasModule.route('/reservaPage', methods=['GET', 'POST'])
def toReservaPage():
    if current_user.is_authenticated:
        print("Noice")
    else:
        print("Not Noice")
    get_Reserva= db.session.query(Ride).all()
    form = AdminForm()
    return render_template("reservas.html", title="Login", get_Reserva = get_Reserva)