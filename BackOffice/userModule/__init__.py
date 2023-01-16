from flask import Blueprint,request
from flask import redirect, render_template, url_for, jsonify
from forms import AdminForm
from models import db , Admin,User,Ride,Vehicle,Reservation
from datetime import datetime
from flask_login import current_user

userModule = Blueprint('userModule', __name__)


@userModule.route('/usersPage', methods=['GET', 'POST'])
def toUsersPage():
    if request.method == 'GET':
        get_Users = db.session.query(User).all()
        return render_template("users.html", title="Login", get_Users = get_Users)
    elif request.method == 'POST':
        id = request.form.get("id")
        
        specify_User = db.session.query(User).filter(User.id==id).first()
        specify_Ride = db.session.query(Ride).filter(Ride.user_id==specify_User.id).first()
        specify_Vehicle = db.session.query(Vehicle).filter(Vehicle.owner_id==specify_User.id).first()
        specify_Reservation = db.session.query(Reservation).filter(Reservation.passenger_id==specify_User.id).first()

        if(specify_Ride != None):
            db.session.delete(specify_Ride)

        if(specify_Vehicle != None):
            db.session.delete(specify_Vehicle)
            
        if(specify_Reservation != None):
            db.session.delete(specify_Reservation)

        db.session.delete(specify_User)
        db.session.commit()
        
    return  jsonify(message="Apagado",status=201)



