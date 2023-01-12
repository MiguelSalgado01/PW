from flask import Blueprint, request
from flask import redirect, render_template, url_for
from forms import VehicleForm
from models import User, db, Vehicle
from flask_login import login_user, logout_user, current_user

addVehicleModule = Blueprint('addVehicleModule', __name__)

@addVehicleModule.route('/addVehicle', methods=['GET', 'POST'])
def adicionarVeiculo():
   vehicleForm = VehicleForm()

   activeUser = current_user
   if current_user.is_authenticated:
      print("Noice")
   else:
      print("Not Noice")

   if request.method == 'POST':
      print(1)
      if vehicleForm.data['goBack']:
         print(2)
         return redirect('verPerfilPage')
      
      if vehicleForm.validate_on_submit() and vehicleForm.regist.data == True:
         vehicle = db.session.query(Vehicle).filter(Vehicle.license_plate == vehicleForm.plate.data).first()
         print(vehicle)
         # if(vehicle == None):
         #    try:
         #       new_user = User(name=form.username.data,student_number=form.student_number.data,phone_number=form.phone_number.data,password=form.password.data,gender=form.user_gender.data)
         #       db.session.add(new_user)
         #       db.session.commit()
         #       return redirect('/login')
         #    except:
         #       return 'error'

         # elif(vehicle != None):
         #    vehicleForm.plate.errors.append("Plate already exists")

   return render_template("registarVeiculo.html", title="Associar Veiculo", frontVehicleForm = vehicleForm)
