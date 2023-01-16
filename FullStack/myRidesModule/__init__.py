from flask import Blueprint, request, jsonify
from flask import redirect, render_template, url_for
from forms import UserRegisterForm, BackButton
from models import User, db, bcrypt, Reservation,Ride,Vehicle,ReservationState
from flask_login import current_user

myRidesModule = Blueprint('myRidesModule', __name__)

@myRidesModule.route('/minhasRides', methods=['GET', 'POST'])
def myrides():
    activeUser = current_user
    goBack = BackButton()
    if activeUser.is_authenticated:
        print("Noice")
    else:
        print("Not Noice")
    
    if request.method == 'GET':  
        getRides_User= db.session.query(Ride).filter(Ride.user_id==activeUser.id).all()
           
        return render_template("myRides.html", goBack = goBack,  getRides_User=getRides_User)

    elif request.method =='POST':
        if goBack.data['goBack']:
            return redirect('homePage')
            # Cancelar Reserva
        if request.form.get("action")== "cancelar":
            idReserva = request.form.get("id")
            print(idReserva)
            specify_Ride = db.session.query(Ride).filter(Ride.id==idReserva).first()
            specify_Resert = db.session.query(Reservation).filter(specify_Ride.id==Reservation.ride_id).first()
            print(specify_Ride)
            print(specify_Resert)
            db.session.delete(specify_Ride)
            db.session.delete(specify_Resert)
            db.session.commit()
            return jsonify(message="Cancelado",status=201)