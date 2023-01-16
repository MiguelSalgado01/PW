from flask import Blueprint,request
from flask import redirect, render_template, url_for,jsonify
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
    if request.method == 'GET':
        get_Ride= db.session.query(Ride).all()
        return render_template("boleias.html", title="Login", get_Ride = get_Ride)
    elif request.method == 'POST':
        id = request.form.get("id")
        print(id)
        specify_Ride = db.session.query(Ride).filter(Ride.id==id).first()
        print(specify_Ride)
        db.session.delete(specify_Ride)
        db.session.commit()
    return  jsonify(message="Apagado",status=201)

