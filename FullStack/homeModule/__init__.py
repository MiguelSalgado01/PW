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
      print(1)
      if homeForm.data['verPerfil']:
         print(2)
         return redirect('logout')
      if homeForm.data['criarBoleia']:
         print(2)
         return redirect('logout')
      if homeForm.data['pesquisar']:
         print(2)
         return redirect('logout')
      if homeForm.data['reservas']:
         print(2)
         return redirect('logout')
      if homeForm.data['endSession']:
         print(2)
         return redirect('logout')
      else:
         return render_template("home.html", title="Home")

   return render_template("home.html", title="Home", frontHomeForm = homeForm, activeUser=activeUser)
