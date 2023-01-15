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
        addReservation = db.session.query(Vehicle, Ride, User, Reservation, ReservationState).filter(
        Reservation.ride_id == Ride.id).filter(Reservation.passenger_id == activeUser.id).filter(
        Reservation.reservation_state_id == ReservationState.id).filter(Ride.vehicle_id == Vehicle.id).filter(
            User.id== Ride.user_id
        ).all()
      
        return render_template("myRides.html", goBack = goBack,addReservation=addReservation)

    elif request.method =='POST':
        if goBack.data['goBack']:
            return redirect('homePage')
            # Cancelar Reserva
        if request.form.get("action")== "cancelar":
            idReserva = request.form.get("id")
            specify_Reservation = db.session.query(Reservation).filter(Reservation.id==idReserva).first()
            print(idReserva)
            #ADD seat extra
            seatsID = db.session.query(Ride).filter(Ride.id==specify_Reservation.ride_id).first()
            print(seatsID)
            seatsID.number_of_available_seats +=1  
            db.session.delete(specify_Reservation)
            db.session.commit()
            return jsonify(message="Cancelado",status=201)
            # Fazer Reserva na Tabela Boleia
        if request.form.get("action")=="reservar":
            id = request.form.get("id")
            searchRide = db.session.query(Ride).filter(Ride.id==id).first()
            getreservaStatus = '1'
           
            vehicle = db.session.query(Vehicle).filter(Vehicle.id == Ride.vehicle_id).first()
            user = db.session.query(User).filter(User.id == Ride.user_id).first()
            reserva_State1 =  db.session.query(ReservationState).filter(ReservationState.id==getreservaStatus).first()
            userIdActive1 = db.session.query(User).filter(User.id==activeUser.id).first()

            new_Reservation = Reservation(passenger_id=userIdActive1.id,ride_id=searchRide.id,reservation_state_id=reserva_State1.id)
            searchRide.number_of_available_seats -=1
            db.session.add(new_Reservation)
            db.session.commit()
            print (new_Reservation)
            return jsonify(message="Adicionado com Suckcess",status=201)
        return  jsonify(message="Açao Nao encontrada",status=404)
    return render_template("myRides.html", goBack = goBack)