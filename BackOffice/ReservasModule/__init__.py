from flask import Blueprint,request
from flask import redirect, render_template, url_for,jsonify
from forms import AdminForm
from models import db , Reservation, User, bcrypt, ReservationState,Ride
from flask_login import login_user, logout_user, current_user
from datetime import datetime

reservaModule = Blueprint('reservaModule', __name__)

@reservaModule.route('/')
def index():
    return redirect('/pages-sign-in')

@reservaModule.route('/reservaPage', methods=['GET', 'POST'])
def toReservaPage():
    if request.method == 'GET':
        get_Reserva= db.session.query(Reservation, ReservationState).filter(Reservation.reservation_state_id == ReservationState.id).all()
        return render_template("reservas.html", title="Login", get_Reserva = get_Reserva)
    elif request.method == 'POST':
        id = request.form.get("id")
        
        specify_Reservation = db.session.query(Reservation).filter(Reservation.id==id).first()
        seatsID = db.session.query(Ride).filter(Ride.id==specify_Reservation.ride_id).first()
            
        seatsID.number_of_available_seats +=1  
        db.session.delete(specify_Reservation)
        db.session.commit()
        
    return  jsonify(message="Apagado",status=201)