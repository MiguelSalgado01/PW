from flask import Blueprint,request
from flask import redirect, render_template, url_for,jsonify
from forms import AdminForm
from models import db , Admin,Ride,Reservation
from datetime import datetime
from flask_login import current_user

rideModule = Blueprint('rideModule', __name__)

@rideModule.route('/ridePage', methods=['GET', 'POST'])
def toRidePage():
    if request.method == 'GET':
        get_Ride= db.session.query(Ride).all()
        return render_template("boleias.html", title="Login", get_Ride = get_Ride)
    elif request.method == 'POST':
        id = request.form.get("id")
        
        specify_Ride = db.session.query(Ride).filter(Ride.id==id).first()
        specify_Resert = db.session.query(Reservation).filter(specify_Ride.id==Reservation.ride_id).first()
        
        db.session.delete(specify_Ride)

        if(specify_Resert != None):
            db.session.delete(specify_Resert)

        db.session.commit()
    return  jsonify(message="Apagado",status=201)

