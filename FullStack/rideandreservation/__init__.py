from flask import Blueprint
from flask import redirect, render_template, url_for,request,jsonify
from flask_login import current_user
from models import Reservation,Ride,db,User,Vehicle,ReservationState

rideandreservation = Blueprint('rideandreservation', __name__)


@rideandreservation.route('/reserva', methods=['GET', 'POST'])
def reservation():
    activeUser = current_user
    if activeUser.is_authenticated:
        print("Noice")
    else:
        print("Not Noice")

    if request.method == 'GET':
        return render_template("reservas.html")
    if request.method =='POST':
        id = request.form.get("id")
        searchRide = db.session.query(Ride).filter(Ride.id==id).first()
        userIdActive = db.session.query(User).filter(User.id==activeUser.id).first()
        getreserva = '1'
        reserva_State =  db.session.query(ReservationState).filter(ReservationState.id==getreserva).first()
        new_Reservation = Reservation(passenger_id=userIdActive.id,ride_id=searchRide.id,reservation_state_id=reserva_State.id)
        searchRide.number_of_available_seats -=1
        db.session.add(new_Reservation)
        db.session.commit()
        
        # return str(buscarid.local_destiny)
        print (new_Reservation)
        return jsonify(message="Adicionado com Suckcess",status=201)
       
@rideandreservation.route('/boleia', methods=['GET', 'POST'])
def ride():
    activeUser = current_user
    if activeUser.is_authenticated:
        print("Noice")
    else:
        print("Not Noice")
    print()
    ridelist = []
    getRideData = db.session.query(Ride).all()
    for ride in getRideData:
        vehicle = db.session.query(Vehicle).filter(Vehicle.id == ride.vehicle_id).first()
        user = db.session.query(User).filter(User.id == ride.user_id).first()
        ridelist.append([(ride.id),(user.name),(vehicle.license_plate),(ride.ride_date),(ride.ride_scheduled_time),(ride.local_destiny),(ride.local_origin),(ride.number_of_available_seats)])
    return render_template("pesquisa.html",getRideData=ridelist)
    
    

        
      

