from flask import Blueprint, request
from flask import redirect, render_template, url_for
from forms import HomeForm
from models import User, db
from flask_login import login_user, logout_user, current_user

homeModule = Blueprint('homeModule', __name__)

@homeModule.route('/homePage', methods=['GET', 'POST'])
def home():
   homeForm = HomeForm()
   activeUser = current_user
   if current_user.is_authenticated:
      print("Noice")
   else:
      print("Not Noice")

   if request.method == 'POST':
      if homeForm.data['verPerfil']:
         return redirect('verPerfilPage')
      elif homeForm.data['criarBoleia']:
         return redirect('makeRides')
      elif homeForm.data['pesquisar']:
         return redirect('logout')
      elif homeForm.data['reservas']:
         return redirect('logout')
      elif homeForm.data['endSession']:
         return redirect('logout')
      else:
         return render_template("home.html", title="Home")

   return render_template("home.html", title="Home", frontHomeForm = homeForm, activeUser=activeUser)
