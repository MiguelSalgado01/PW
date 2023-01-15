from flask import Blueprint, request
from flask import redirect, render_template, url_for
from forms import UserLoginForm
from models import User, db, bcrypt
from flask_login import login_user, logout_user, current_user
from datetime import datetime

loginModule = Blueprint('loginModule', __name__)

@loginModule.route('/')
def index():
   return redirect('/login')

@loginModule.route('/login', methods=['GET', 'POST'])
def doLogin():
   form = UserLoginForm()
   
   if request.method == 'POST':

      if form.validate_on_submit() and form.login.data == True:
         user = db.session.query(User).filter(User.student_number == form.student_number.data).first()
         if(user==None):
            form.student_number.errors.append("Incorrect Student Number")
         else:
            if(bcrypt.check_password_hash(user.password, form.password.data)):
               try:
                  user.active = True
                  user.last_login_date = datetime.now()
                  db.session.commit()
                  login_user(user)
                  return redirect('/homePage')
               except:
                     return 'error'
            else:
               form.password.errors.append("Incorrect Password")
      

      elif form.toRegist.data == True:
         return redirect('/registar')

   
   return render_template("login.html", title="Login", formFront=form)

@loginModule.route('/logout')
def logOut():
   logout_user()
   return redirect('login')