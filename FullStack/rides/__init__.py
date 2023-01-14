import json
from flask import Blueprint, request, redirect, render_template
from forms import RideForm
from models import Vehicle, Ride, db
from flask_login import current_user

rides = Blueprint('rides', __name__)

@rides.route('/makeRides', methods=['GET', 'POST'])
def toMakeRides():
    rideForm = RideForm()
    activeUser = current_user

    if current_user.is_authenticated:
        vehicle = db.session.query(Vehicle).filter(Vehicle.owner_id == activeUser.id).all()
        vehicle_group_list=[(str(i.id), i.license_plate) for i in vehicle]
        presets_group_list = [(' ',"Selecionar Veiculo"), ('0',"Sem Veiculo")]

        for transport in vehicle_group_list:
            presets_group_list.append(transport)

        rideForm.vehicle.choices = presets_group_list
        

        if(request.method == 'POST'):

            if(rideForm.vehicle.data == '0'):
                return redirect('addVehicle')
            
            if rideForm.data['goBack']:
                return redirect('homePage')
            

            if rideForm.validate_on_submit():
                switchValue = defineComeAndGo(rideForm.place.data)
                
                for transport in rideForm.vehicle.choices:
                    if transport[0] == rideForm.vehicle.data:
                        valuePlate = transport[1]

                vehicle = db.session.query(Vehicle).filter(Vehicle.license_plate == valuePlate).first()

                try:
                    new_ride = Ride(user_id = activeUser.id, vehicle_id=vehicle.id, 
                        ride_date=str(rideForm.date.raw_data)[2:12],ride_scheduled_time=str(rideForm.hora.data)[0:5],
                        local_origin=switchValue[0], local_destiny = switchValue[1], number_of_available_seats= vehicle.number_of_seats)
                    db.session.add(new_ride)
                    print(new_ride)
                    db.session.commit()
                    return redirect('homePage')

                except  Exception as e:
                    print(str(e))

        return render_template("criaBoleia.html", title="Criar Boleia", frontRideForm=rideForm)

    else:
        print("Not Noice")
    
    return render_template("criaBoleia.html", title="Criar Boleia", frontRideForm=rideForm)

def defineComeAndGo(place):
    processedValue = processString(json.dumps(str(request.data)))

    if(processedValue == 'Destino'):
         comeGo_list=[('ISMAT'), (place)]
    else:
         comeGo_list=[(place), ('ISMAT')]
    
    print(comeGo_list)
    return comeGo_list

def processString(value):
    value = value.replace('b', '')   
    value = value.replace("'", '')
    value = value.replace('"', '')
    if value == '': value = 'Destino'
    return value