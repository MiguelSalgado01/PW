from flask import Blueprint
from flask import redirect, render_template, url_for
from models import Reservation,Ride,db,User

modulo3 = Blueprint('modulo3', __name__)


@modulo3.route('/reserva', methods=['GET', 'POST'])
def reservation():
    return render_template("reservas.html")

@modulo3.route('/boleia', methods=['GET', 'POST'])
def ride():
    #return render_template("pesquisa.html")
    #getUserData = db.session.query(User).all()
    getUserData = db.session.query(User).all()
    return render_template("pesquisa.html",getUserData=getUserData)

        
      

