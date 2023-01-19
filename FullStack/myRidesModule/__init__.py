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
        if request.method == 'GET':  
            getRides_User= db.session.query(Ride).filter(Ride.user_id==activeUser.id).filter(Ride.deleted!=True).all()
            
            return render_template("myRides.html", goBack = goBack,  getRides_User=getRides_User)

        elif request.method =='POST':
            if goBack.data['goBack']:
                return redirect('homePage')
                # Cancelar Reserva
            if request.form.get("action") == "cancelar":
                idRide = request.form.get("id")
                
                specify_Ride = db.session.query(Ride).filter(Ride.id==idRide).first()
                specify_Resert = db.session.query(Reservation).filter(specify_Ride.id==Reservation.ride_id).all()

                if(specify_Ride != None):
                    specify_Ride.deleted = True

                if(specify_Resert != []):
                    for reserva in specify_Resert:
                        reserva.deleted = True
                        reserva.reservation_state_id = 3

                db.session.commit()
                return jsonify(message="Cancelado",status=201)

    else:
        print("Not Noice")
    

    