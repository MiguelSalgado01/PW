from flask import Blueprint,request
from flask import redirect, render_template, url_for, jsonify
from models import Vehicle, db, User
from flask_login import current_user

vehicleModule = Blueprint('vehicleModule', __name__)

@vehicleModule.route('/vehiclesPage', methods=['GET', 'POST'])
def toVehiclesPage():
    if current_user.is_authenticated:
        try:
            activeUser =  db.session.query(User).filter(User.id==current_user.id).first()

            if request.method == 'GET':
                veiculos = db.session.query(User,Vehicle).filter(Vehicle.owner_id==User.id).all()

                return render_template("vehicles.html", title="Login", veiculos = veiculos, activeUser = activeUser)
            
            elif request.method == 'POST':
                id = request.form.get("id")
                specify_Vehicle = db.session.query(Vehicle).filter(Vehicle.id==id).first()
                    
                if(specify_Vehicle != None):
                    specify_Vehicle.deleted = True

                db.session.commit()
              
            return  jsonify(message="Apagado",status=201)
        
        except Exception as e:
            print(str(e))

    else:
        return redirect('/pages-sign-in')
      
   
        
