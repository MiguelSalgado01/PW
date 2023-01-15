from flask import Blueprint, request
from flask import redirect, render_template, url_for
from forms import HomeForm
from models import User, db, Ride, Reservation
from flask_login import login_user, logout_user, current_user

homeModule = Blueprint('homeModule', __name__)

@homeModule.route('/homePage', methods=['GET', 'POST'])
def home():
   homeForm = HomeForm()
   activeUser = current_user
   if current_user.is_authenticated:
      print("Noice")
   else:
      print("Not Noice")
   
   userRides = db.session.query(Ride).filter(Ride.user_id==activeUser.id).all()
   userReservations = db.session.query(Reservation).filter(Reservation.passenger_id==activeUser.id).all()
   
   rideCount = 0
   for ride in userRides:
      rideCount+=1

   reservationCount = 0
   for reservation in userReservations:
      reservationCount+=1

   nextReservations = db.session.query(Reservation,Ride,User).filter(Ride.id==Reservation.ride_id).filter(Reservation.passenger_id==activeUser.id).filter(User.id==Ride.user_id).order_by(Ride.ride_scheduled_time.desc()).limit(4).all()

   for rese in nextReservations:
      print(rese.Ride.ride_date)
   
# userReservations.order_by(Reservation)

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
