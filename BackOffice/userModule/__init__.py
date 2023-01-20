from flask import Blueprint,request
from flask import redirect, render_template, url_for, jsonify
from forms import AdminForm
from models import db , Admin,User,Ride,Vehicle,Reservation,bcrypt
from datetime import datetime
from flask_login import current_user

userModule = Blueprint('userModule', __name__)


@userModule.route('/usersPage', methods=['GET', 'POST'])
def toUsersPage():
    if current_user.is_authenticated:
        try:
            use_id = current_user.id
            activeUser =  db.session.query(User).filter(User.id==use_id).first()

            if request.method == 'GET':
                get_Users = db.session.query(User).all()
                return render_template("users.html", title="Login", get_Users = get_Users, activeUser = activeUser)

            elif request.method == 'POST':
                if request.form.get("action")=="Apagar":
                    id = request.form.get("id")
                
                    specify_User = db.session.query(User).filter(User.id==id).first()
                    specify_Ride = db.session.query(Ride).filter(Ride.user_id==specify_User.id).all()
                    specify_Vehicle = db.session.query(Vehicle).filter(Vehicle.owner_id==specify_User.id).all()
                    specify_Reservation = db.session.query(Reservation).filter(Reservation.passenger_id==specify_User.id).all()

                    if(specify_Reservation != []):
                        deleteReserva(specify_Reservation)
                        
                    if(specify_Ride != None):
                        for ride in specify_Ride:
                            ride.deleted = True
                            rideWithReservation = db.session.query(Reservation).filter(Reservation.ride_id==ride.id).all()
                            deleteReserva(rideWithReservation)

                    
                    if(specify_Vehicle != None):
                        for vehicle in specify_Vehicle:
                            vehicle.deleted = True

                    specify_User.deleted = True
                    db.session.commit()

                    return jsonify(message="Apagado", status=201)

                if request.form.get("action")=="Editar":
                    idUser = request.form.get("id")
                    userEdit = db.session.query(User).filter(User.id==idUser).first()
                    user = {
                        "id": userEdit.id,
                        "name": userEdit.name,
                        "student_number": userEdit.student_number,
                        "phone_number": userEdit.phone_number
                    }
                    return jsonify(user)

                if request.form.get("action")=="editsave":
                    idUser = request.form.get("id")
                    userquery = db.session.query(User).filter(User.id==idUser).first()
                    if request.form.get("name")!= '':
                        userquery.name=request.form.get("name")
                    if request.form.get("student_number")!= '':
                        userquery.student_number=request.form.get("student_number")
                    if request.form.get("phone_number")!= '':
                        if(len(request.form.get("phone_number")) != 9):
                            return jsonify(message="Phone number tem de ser 9!!")
                        userquery.phone_number=request.form.get("phone_number")
                    if request.form.get("password") != '':
                        if(len(request.form.get("password")) < 8 or len(request.form.get("password")) > 20):
                            return jsonify(message="Password nÃ£o pode ser menor de 8 e maior que 20!!")
                        userquery.password=bcrypt.generate_password_hash(request.form.get("password"))
                        
                    db.session.add(userquery)
                    db.session.commit()

                    return jsonify(message="Atualizado")

        except Exception as e:
            print(str(e))

    else:
        return redirect('/pages-sign-in')

def deleteReserva(reservas):
    for reserva in reservas:
        reserva.deleted = True
        reserva.reservation_state_id = 3