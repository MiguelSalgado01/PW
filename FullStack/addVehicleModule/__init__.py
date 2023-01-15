from flask import Blueprint, request
from flask import redirect, render_template, url_for
from forms import VehicleForm
from models import db, Vehicle
from flask_login import current_user

addVehicleModule = Blueprint('addVehicleModule', __name__)

@addVehicleModule.route('/addVehicle', methods=['GET', 'POST'])
def adicionarVeiculo():
   vehicleForm = VehicleForm()
   activeUser = current_user
   userId = activeUser.id

   if request.method == 'POST' and activeUser.is_authenticated:
      print(userId)
      if vehicleForm.data['goBack']:
         return redirect('verPerfilPage')
      
      if vehicleForm.validate_on_submit() and vehicleForm.regist.data == True:
         vehicle = db.session.query(Vehicle).filter(Vehicle.license_plate == vehicleForm.plate.data).first()
         print(vehicle)
         if(vehicle == None):
            try:
               new_vehicle = Vehicle(owner_id = activeUser.id, license_plate=vehicleForm.plate.data, 
                  color=vehicleForm.color.data,number_of_seats=vehicleForm.sits.data,
                  vehicle_specs = vehicleForm.Specs.data)
               db.session.add(new_vehicle)
               db.session.commit()
               return redirect('verPerfilPage')

            except:
               return 'error'

         elif(vehicle != None):
            vehicleForm.plate.errors.append("Plate already exists")

   return render_template("registarVeiculo.html", title="Associar Veiculo", frontVehicleForm = vehicleForm)
