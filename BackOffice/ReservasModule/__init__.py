from flask import Blueprint,request
from flask import redirect, render_template, url_for
from forms import AdminForm
from models import db , Reservation, User, bcrypt, ReservationState
from flask_login import login_user, logout_user, current_user
from datetime import datetime

reservaModule = Blueprint('reservaModule', __name__)

@reservaModule.route('/')
def index():
    return redirect('/pages-sign-in')

@reservaModule.route('/reservaPage', methods=['GET', 'POST'])
def toReservaPage():
    if current_user.is_authenticated:
        print("Noice")
    else:
        print("Not Noice")
    get_Reserva= db.session.query(Reservation, ReservationState).filter(Reservation.reservation_state_id == ReservationState.id).all()
    form = AdminForm()
    return render_template("reservas.html", title="Login", get_Reserva = get_Reserva)