from flask import Blueprint, request
from flask import redirect, render_template, url_for
from forms import ProfileForm
from models import User, db
from flask_login import login_user, logout_user, current_user

verPerfilModule = Blueprint('verPerfilModule', __name__)

@verPerfilModule.route('/verPerfilPage', methods=['GET', 'POST'])
def verPerfil():
   profileForm = ProfileForm()
   activeUser = current_user
   if current_user.is_authenticated:
      print("Noice")
   else:
      print("Not Noice")

   if request.method == 'POST':
      if profileForm.data['goBack']:
         return redirect('homePage')

      if profileForm.data['editarPerfil']:
         return redirect('editProfile')

      if profileForm.data['adicionarVeiculo']:
         return redirect('addVehicle')
      
      if profileForm.data['seeVehicle']:
         return redirect('seeVehicle')
         
      else:
         return render_template("verPerfil.html", title="Ver Perfil")

   return render_template("verPerfil.html", title="Ver Perfil", frontProfileForm = profileForm, activeUser=activeUser)
