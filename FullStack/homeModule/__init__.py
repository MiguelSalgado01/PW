from flask import Blueprint, request
from flask import redirect, render_template, url_for
from forms import UserRegisterForm
from models import User, db
from flask_login import login_user, logout_user, current_user

homeModule = Blueprint('homeModule', __name__)

@homeModule.route('/homePage', methods=['GET', 'POST'])
def home():
   if current_user.is_authenticated:
      print("Noice")
   return render_template("home.html")
