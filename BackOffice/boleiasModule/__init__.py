from flask import Blueprint,request
from flask import redirect, render_template, url_for
from forms import AdminForm
from models import db , Admin,Ride
from datetime import datetime
from flask_login import current_user

rideModule = Blueprint('rideModule', __name__)

@rideModule.route('/ridePage', methods=['GET', 'POST'])
def toRidePage():
    if current_user.is_authenticated:
        print("Noice")
    else:
        print("Not Noice")
    get_Ride= db.session.query(Ride).all()
    form = AdminForm()
    return render_template("boleias.html", title="Login", get_Ride = get_Ride)



