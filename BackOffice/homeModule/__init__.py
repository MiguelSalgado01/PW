from flask import Blueprint,request
from flask import redirect, render_template, url_for
from forms import AdminForm
from models import db , Admin,User, Ride, Reservation
from datetime import datetime
from flask_login import current_user

homeModule = Blueprint('homeModule', __name__)


@homeModule.route('/homePage', methods=['GET', 'POST'])
def toHomePage():
    if current_user.is_authenticated:
        print("Noice")
    else:
        print("Not Noice")

    get_Users = db.session.query(User).all()
    allRides = db.session.query(Ride).all()
    allReservations = db.session.query(Reservation).all()
    form = AdminForm()
    return render_template("home.html", title="Login", get_Users = get_Users, allRides = allRides, allReservations = allReservations)



