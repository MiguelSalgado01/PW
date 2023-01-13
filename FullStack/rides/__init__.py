from flask import Blueprint, jsonify, request
from flask import redirect, render_template, url_for
from forms import RideForm
from models import Vehicle, Ride, db, ReservationState
from flask_login import login_user, logout_user, current_user

rides = Blueprint('rides', __name__)

@rides.route('/makeRides', methods=['GET', 'POST'])
def toMakeRides():
    rideForm = RideForm()
    activeUser = current_user
    switch = ''

    if current_user.is_authenticated:
        vehicle = db.session.query(Vehicle).filter(Vehicle.owner_id == activeUser.id).all()
        vehicle_group_list=[(str(i.id), i.license_plate) for i in vehicle]
        presets_group_list = [(' ',"Selecionar Veiculo"), ('0',"Sem Veiculo")]

        for transport in vehicle_group_list:
            presets_group_list.append(transport)

        rideForm.vehicle.choices = presets_group_list


        if(request.method == 'POST'):

            defineComeAndGo()
        

            if(rideForm.vehicle.data == '0'):
                return redirect('addVehicle')
            
            elif rideForm.data['goBack']:
                return redirect('homePage')

            if rideForm.validate_on_submit():
                
                for transport in rideForm.vehicle.choices:
                    if transport[0] == rideForm.vehicle.data:
                        valuePlate = transport[1]

                print(valuePlate + " " + str(rideForm.date.raw_data)[2:12] + " " +  str(rideForm.hora.data)[0:5] + " " + rideForm.place.data + " " + rideForm.pref.data)
                
                vehicle = db.session.query(Vehicle).filter(Vehicle.license_plate == valuePlate).first()
                print(vehicle.number_of_seats)

                try:
                    new_ride = Ride(user_id = activeUser.id, vehicle_id=vehicle.id, 
                        ride_date=str(rideForm.date.raw_data)[2:12],ride_scheduled_time=str(rideForm.hora.data)[0:5],
                        local_destiny = "Lagoa", local_origin="ISMAT", number_of_available_seats= vehicle.number_of_seats)
                    db.session.add(new_ride)
                    print(new_ride)
                    db.session.commit()
                    return redirect('homePage')

                except  Exception as e: # work on python 3.x
                    print(str(e))

        return render_template("criaBoleia.html", title="Criar Boleia", frontRideForm=rideForm)

    else:
        print("Not Noice")
    
    return render_template("criaBoleia.html", title="Criar Boleia", frontRideForm=rideForm)

def defineComeAndGo():
    jsonData = request.get_json()
    print (jsonData['switch'])
    comeGo_list=[("origem", ''), ("destino", '')]

    if(jsonData['switch'] == 'Destino'):
        print(comeGo_list[0][1])
# from flask import Blueprint
# from flask import redirect, render_template, url_for
# from forms import UserRegisterForm

# modulo2 = Blueprint('modulo2', __name__)

# @modulo2.route('/registar', methods=['GET', 'POST'])
# def register():
#     form = UserRegisterForm()

#     if request.method == 'POST':
#         if form.validate_on_submit():
#             verifyStudentNumb = db.session.query(User).filter(User.student_number == form.student_number.data).first()
#             verifyUsername = db.session.query(User).filter(User.name == form.username.data).first()
#             if(verifyStudentNumb == None and verifyUsername == None):
#                 try:
#                     new_user = User(name=form.username.data,student_number=form.student_number.data,phone_number=form.phone_number.data,password=form.password.data,gender=form.user_gender.data)
#                     db.session.add(new_user)
#                     db.session.commit()
#                     return redirect('/login')
#                 except:
#                     return 'error'
                    
#             elif(verifyStudentNumb != None and verifyUsername != None):
#                 form.student_number.errors.append("Student number already exists")
#                 form.username.errors.append("Username number already exists")
#             elif(verifyStudentNumb != None):
#                 form.student_number.errors.append("Student number already exists")
#             elif(verifyUsername != None):
#                 form.username.errors.append("Username number already exists")
        
#         elif request.form['LogBtn'] == 'Tenho Conta':
#             return redirect('/login')
       
#     elif request.method == 'GET': 
#         return render_template("registarUser.html", title="Criar Boleia", form=form)
  