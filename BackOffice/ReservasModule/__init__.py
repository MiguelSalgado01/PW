from flask import Blueprint,request
from flask import redirect, render_template, url_for,jsonify
from forms import AdminForm
from models import db , Reservation, User, bcrypt, ReservationState, Ride
from flask_login import login_user, logout_user, current_user
from datetime import datetime
from sqlalchemy import text

reservaModule = Blueprint('reservaModule', __name__)

@reservaModule.route('/')
def index():
    return redirect('/pages-sign-in')

@reservaModule.route('/reservaPage', methods=['GET', 'POST'])
def toReservaPage():
    reserva = []

    if current_user.is_authenticated:
        try:
            use_id = current_user.id
            activeUser =  db.session.query(User).filter(User.id==use_id).first()

            if request.method == 'GET':
                sql_query = text('SELECT condutor.name as condutor, passageiro.name as passageiro, reservation.ride_id as ride, \
                    reservation_state.state as status, reservation.createdAt as dataCriacao, reservation.updatedAt as dataUpdate, reservation.id as idReserva \
                    FROM user as condutor, user as passageiro, reservation, reservation_state \
                    JOIN ride ON reservation.ride_id == ride.id \
                    where passageiro.id == reservation.passenger_id and condutor.id == ride.user_id and reservation.reservation_state_id == reservation_state.id  \
                    ')
                reservas = db.session.execute(sql_query)
                for r in reservas:
                    reserva.append(((r.condutor), (r.passageiro), (r.ride), (r.status), (datetime.strptime(r.dataCriacao[0:19], '%Y-%m-%d %H:%M:%S')), (datetime.strptime(r.dataUpdate[0:19], '%Y-%m-%d %H:%M:%S')), (r.idReserva)))
                    print(r.condutor + " " + r.passageiro + " " + str(r.ride) + " " + r.status + " " + r.dataCriacao + " " + r.dataUpdate + " " + str(r.idReserva))
          
                return render_template("reservas.html", title="Login", reserva = reserva, activeUser = activeUser)
            elif request.method == 'POST':
                id = request.form.get("id")
                
                specify_Reservation = db.session.query(Reservation).filter(Reservation.id==id).first()
                seatsID = db.session.query(Ride).filter(Ride.id==specify_Reservation.ride_id).first()
                seatsID.number_of_available_seats +=1  
                
                db.session.delete(specify_Reservation)
                db.session.commit()
                
            return  jsonify(message="Apagado",status=201)
        
        except Exception as e:
            print(str(e))

    else:
        return redirect('/pages-sign-in')
      
   
        
