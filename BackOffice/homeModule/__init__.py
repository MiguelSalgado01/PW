from flask import Blueprint,request
from flask import redirect, render_template, url_for
from forms import AdminForm
from models import db , Admin,User, Ride, Reservation, Vehicle
from datetime import datetime
from flask_login import current_user

homeModule = Blueprint('homeModule', __name__)


@homeModule.route('/homePage', methods=['GET', 'POST'])
def toHomePage():
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

    ridesFormated = []

    # for us in allUsers:
    #     print(us)

    for rs in allRides:
        print(rs)
        datetime_object = datetime.strptime(rs.ride_date, "%Y-%M-%d").date()
        rs.ride_date = datetime_object

    # for res in allReservations:
    #     print(res)

    form = AdminForm()
    return render_template("home.html", title="Login", allUsers = allUsers, allRides = allRides, 
        allReservations = allReservations, allRidesCount = allRidesCount, allReservationsCount = allReservationsCount, 
        allVehiclesCount = allVehiclesCount, allUsersCount = allUsersCount, activeUser = activeUser)



