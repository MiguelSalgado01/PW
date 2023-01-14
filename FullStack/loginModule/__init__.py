from flask import Blueprint, request
from flask import redirect, render_template, url_for
from forms import UserLoginForm
from models import User, db
from flask_login import login_user, logout_user, current_user

loginModule = Blueprint('loginModule', __name__)

@loginModule.route('/')
def index():
   return redirect('/login')

@loginModule.route('/login', methods=['GET', 'POST'])
def doLogin():
   if current_user.is_authenticated:
      print("Noice")
   else:
      print("Not Noice")

   form = UserLoginForm()
   
   if request.method == 'POST':
      print(form.login.data)
      print(form.toRegist.data)

      if form.validate_on_submit() and form.login.data == True:
         user = db.session.query(User).filter(User.student_number == form.student_number.data).first()
         if(user==None):
            form.student_number.errors.append("Incorrect Student Number")
         else:
            if(user.password == form.password.data):
               try:
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