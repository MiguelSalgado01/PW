from flask import Blueprint
from flask import redirect, render_template, url_for,request
from models import Reservation,Ride,db,User,Vehicle

rideandreservation = Blueprint('rideandreservation', __name__)


@rideandreservation.route('/reserva', methods=['GET', 'POST'])
def reservation():
    if request.method == 'GET':
        return render_template("reservas.html")
    if request.method =='POST':
        id = request.form.get("id")
        buscarid = db.session.query(Ride).filter(Ride.id==id).first()
        return str(buscarid.id), 201

@rideandreservation.route('/boleia', methods=['GET', 'POST'])
def ride():
    ridelist = []
    getRideData = db.session.query(Ride).all()
    for ride in getRideData:
        vehicle = db.session.query(Vehicle).filter(Vehicle.id == ride.vehicle_id).first()
        user = db.session.query(User).filter(User.id == ride.user_id).first()
        ridelist.append([(ride.id),(user.name),(vehicle.license_plate),(ride.ride_date),(ride.ride_scheduled_time),(ride.local_destiny),(ride.local_origin),(ride.number_of_available_seats)])
    return render_template("pesquisa.html",getRideData=ridelist)
    
    

        
      

