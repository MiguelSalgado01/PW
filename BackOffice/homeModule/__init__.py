from flask import Blueprint,request
from flask import redirect, render_template, url_for
from forms import AdminForm
from models import db , Admin, User, Ride, Reservation, Vehicle
from sqlalchemy import func, desc
from datetime import datetime
from flask_login import current_user

homeModule = Blueprint('homeModule', __name__)



@homeModule.route('/homePage', methods=['GET', 'POST'])
def toHomePage():
    dates = []
    graf_topVehicles = []

    if current_user.is_authenticated:
        print("Noice")
    else:
        print("Not Noice")

    use_id = current_user.id

    activeUser =  db.session.query(User).filter(User.id==use_id).first()

    allUsers = db.session.query(User).all()
    allRides = db.session.query(Ride).all()
    allReservations = db.session.query(Reservation).all()
    allVehicles = db.session.query(Vehicle).all()

    allUsersCount = len(allUsers)
    allRidesCount = len(allRides)
    allReservationsCount = len(allReservations)
    allVehiclesCount = len(allVehicles)

    for rs in allRides:
        datetime_object = datetime.strptime(rs.ride_date, "%Y-%m-%d").date()
        rs.ride_date = datetime_object
        dates.append(rs.ride_date.month)
    
    graf_dataBoleias = [("Jan", dates.count(1)), ("Fev", dates.count(2)),("Mar", dates.count(3)), ("Abr", dates.count(4)),
        ("Mai", dates.count(5)), ("Jun", dates.count(6)),("Jul", dates.count(7)), ("Ago", dates.count(8)),
        ("Set", dates.count(9)), ("Out", dates.count(10)),("Nov", dates.count(11)), ("Dez", dates.count(12)),]


    topVehicles = db.session.query(Ride,func.count(Ride.vehicle_id).label('qty')).group_by(Ride.vehicle_id).order_by(desc('qty')).limit(3).all()

    for v in topVehicles:
        print(v.Ride.vehicle_id)
        vehiclePerRide = db.session.query(Vehicle).filter(v.Ride.vehicle_id == Vehicle.id).first()
        print(vehiclePerRide.license_plate)
        graf_topVehicles.append((vehiclePerRide.license_plate, v.qty))

    print(graf_topVehicles)
    print(topVehicles[0].qty)
    print(topVehicles[1].qty)
    print(topVehicles[2].qty)

    form = AdminForm()
    return render_template("home.html", title="Login", allRidesCount = allRidesCount, allReservationsCount = allReservationsCount, 
        allVehiclesCount = allVehiclesCount, allUsersCount = allUsersCount, activeUser = activeUser, 
        graf_dataBoleias = graf_dataBoleias, graf_topVehicles = graf_topVehicles)



