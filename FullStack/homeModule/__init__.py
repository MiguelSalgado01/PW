from flask import Blueprint, request
from flask import redirect, render_template, url_for
from forms import HomeForm
from models import User, db, Ride, Reservation,Vehicle,ReservationState
from flask_login import login_user, logout_user, current_user

homeModule = Blueprint('homeModule', __name__)

@homeModule.route('/homePage', methods=['GET', 'POST'])
def home():
   homeForm = HomeForm()
   activeUser = current_user
   
   userRides = db.session.query(Ride).filter(Ride.user_id==activeUser.id).all()
   userReservations = db.session.query(Reservation).filter(Reservation.passenger_id==activeUser.id).all()
   
   rideCount = len(userRides)
   reservationCount = len(userReservations)
  
   nextReservations = db.session.query(Vehicle, Ride, User, Reservation, ReservationState).filter(
        Reservation.ride_id == Ride.id).filter(Reservation.passenger_id == activeUser.id).filter(
        Reservation.reservation_state_id == ReservationState.id).filter(Ride.vehicle_id == Vehicle.id).filter(
         User.id== Ride.user_id).order_by(Ride.ride_scheduled_time.desc()).limit(4).all()

   graf_data = [(rideCount,"Boleias Dadas"), (reservationCount,"Reservas Feitas")]

   if request.method == 'POST':
      if homeForm.data['verPerfil']:
         return redirect('verPerfilPage')

      elif homeForm.data['criarBoleia']:
         return redirect('makeRides')

      elif homeForm.data['pesquisar']:
         return redirect('boleia')

      elif homeForm.data['reservas']:
         return redirect('reserva')

      elif homeForm.data['endSession']:
         return redirect('logout')
      else:
         return render_template("home.html", title="Home")

   return render_template("home.html", title="Home", frontHomeForm = homeForm, activeUser=activeUser, frontReservations = nextReservations, frontReservationCount = graf_data)
