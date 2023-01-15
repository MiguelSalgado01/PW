from flask import Blueprint
from flask import redirect, render_template, url_for, request, jsonify
from flask_login import current_user
from models import Reservation,Ride,db,User,Vehicle,ReservationState
from forms import BackButton

rideandreservation = Blueprint('rideandreservation', __name__)


@rideandreservation.route('/reserva', methods=['GET', 'POST'])
def reservation():
    activeUser = current_user
    
    get_Reservas = db.session.query(Reservation).filter(Reservation.passenger_id==activeUser.id)
    goBack = BackButton()
    if activeUser.is_authenticated:
        print("Noice")
    else:
        print("Not Noice")
    
    if request.method == 'GET':  
        return render_template("reservas.html", goBack = goBack,get_Reservas=get_Reservas)

    elif request.method =='POST':
        if goBack.data['goBack']:
            return redirect('homePage')
            # Cancelar Reserva
        if request.form.get("action")== "cancelar":
            idReserva = request.form.get("id")
            specify_Reservation = db.session.query(Reservation).filter(Reservation.id==idReserva).first()
            #ADD seat extra
            seatsID = db.session.query(Ride).filter(Ride.id==specify_Reservation.ride_id).first()
            seatsID.number_of_available_seats +=1  
            db.session.delete(specify_Reservation)
            db.session.commit()
            return jsonify(message="Cancelado",status=201)
            # Fazer Reserva na Tabela Boleia
        if request.form.get("action")=="reservar":
            id = request.form.get("id")
            searchRide = db.session.query(Ride).filter(Ride.id==id).first()

            vehicle = db.session.query(Vehicle).filter(Vehicle.id == Ride.vehicle_id).first()
            user = db.session.query(User).filter(User.id == Ride.user_id).first()
            
            # userIdActive = db.session.query(User).filter(User.id==activeUser.id).first()
            # getreservaStatus = '1'
            # reserva_State =  db.session.query(ReservationState).filter(ReservationState.id==getreservaStatus).first()
            # addReservation = db.session.query(Reservation,Ride,User).filter(Ride.id==Reservation.ride_id).filter(Reservation.passenger_id==activeUser.id).filter(User.id==Ride.user_id).order_by(Ride.ride_scheduled_time.desc()).limit(4).all()
            # #new_Reservation = Reservation(passenger_id=userIdActive.id,ride_id=searchRide.id,reservation_state_id=reserva_State.id)
            new_Reservation = Reservation(user.name,vehicle.license_plate,searchRide.ride_date,
            searchRide.ride_scheduled_time,searchRide.local_destiny,searchRide.local_origin)
            searchRide.number_of_available_seats -=1
            db.session.add(new_Reservation)
            db.session.commit()
            print (new_Reservation)
            return jsonify(message="Adicionado com Suckcess",status=201)
        return  jsonify(message="Açao Nao encontrada",status=404)
    return render_template("reservas.html", goBack = goBack)
       
@rideandreservation.route('/boleia', methods=['GET', 'POST'])
def ride():
    activeUser = current_user
    if activeUser.is_authenticated:
        print("Noice")
    else:
        print("Not Noice")
        
    goBack = BackButton()
    ridelist = []
    getRideData = db.session.query(Ride).all()

    if goBack.data['goBack']:
        return redirect('homePage')
    # Mostrar Dados na Table Boleia
    for ride in getRideData:
        vehicle = db.session.query(Vehicle).filter(Vehicle.id == ride.vehicle_id).first()
        user = db.session.query(User).filter(User.id == ride.user_id).first()
        ridelist.append([(ride.id),(user.name),(vehicle.license_plate),(ride.ride_date),(ride.ride_scheduled_time),(ride.local_destiny),(ride.local_origin),(ride.number_of_available_seats)])
    return render_template("pesquisa.html",getRideData=ridelist, goBack=goBack)
    

   
       
      

