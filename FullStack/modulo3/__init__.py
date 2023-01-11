from flask import Blueprint
from flask import redirect, render_template, url_for
from models import Reservation

modulo3 = Blueprint('modulo3', __name__)


@modulo3.route('/reserva', methods=['GET', 'POST'])
def reservation():
    return render_template("reservas.html")