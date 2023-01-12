from flask import Blueprint
from flask import redirect, render_template, url_for
from models import Reservation,Ride,db,User

rideandreservation = Blueprint('rideandreservation', __name__)


@rideandreservation.route('/reserva', methods=['GET', 'POST'])
def reservation():
    return render_template("reservas.html")

@rideandreservation.route('/boleia', methods=['GET', 'POST'])
def ride():
    #return render_template("pesquisa.html")
    #getUserData = db.session.query(User).all()
    getUserData = db.session.query(User).all()
    return render_template("pesquisa.html",getUserData=getUserData)

        
      

