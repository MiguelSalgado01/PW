from flask import Blueprint, request
from flask import redirect, render_template, url_for
from forms import HomeForm
from models import User, db
from flask_login import login_user, logout_user, current_user

editProfileModule = Blueprint('editProfileModule', __name__)

@editProfileModule.route('/editProfile', methods=['GET', 'POST'])
def home():
   activeUser = current_user
   if current_user.is_authenticated:
      print("Noice")
   else:
      print("Not Noice")

   return render_template("editorPerfil.html", title="Editar Perfil")
