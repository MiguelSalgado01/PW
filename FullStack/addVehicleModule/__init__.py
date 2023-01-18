from flask import Blueprint, request
from flask import redirect, render_template, url_for,jsonify
from forms import VehicleForm,BackButton
from models import db, Vehicle,Ride,Reservation
from flask_login import current_user

addVehicleModule = Blueprint('addVehicleModule', __name__)

@addVehicleModule.route('/addVehicle', methods=['GET', 'POST'])
def adicionarVeiculo():
   vehicleForm = VehicleForm()
   activeUser = current_user
   userId = activeUser.id

   if request.method == 'POST' and activeUser.is_authenticated:
      
      if vehicleForm.data['goBack']:
         return redirect('verPerfilPage')
      
      if vehicleForm.validate_on_submit() and vehicleForm.regist.data == True:
         vehicle = db.session.query(Vehicle).filter(Vehicle.license_plate == vehicleForm.plate.data).first()
         
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


@addVehicleModule.route('/seeVehicle', methods=['GET', 'POST'])
def seeVehicle():
   vehicleForm = VehicleForm()
   activeUser = current_user
   if request.method == 'POST':
      
      if vehicleForm.data['goBack']:
            return redirect('verPerfilPage')
      
   queryVehicleUser = db.session.query(Vehicle).filter(Vehicle.owner_id==activeUser.id)

   if request.form.get("action") == "apagar":
                id = request.form.get("id")
                
                specify_Ride = db.session.query(Ride).filter(Ride.id==idRide).first()
                specify_Resert = db.session.query(Reservation).filter(specify_Ride.id==Reservation.ride_id).first()
               #  db.session.delete(specify_Ride)
               #  if(specify_Resert != None):
               #      db.session.delete(specify_Resert)

               #  db.session.commit()
                return jsonify(message="Viatura Apagado Com Sucesso",status=201)

   return render_template("myVehicles.html",frontVehicleForm = vehicleForm,queryVehicleUser=queryVehicleUser)