from flask import Blueprint, request
from flask import redirect, render_template, url_for
from forms import UserLoginForm
from models import User, db
from flask_login import login_user, logout_user, current_user

modulo1 = Blueprint('modulo1', __name__)

@modulo1.route('/')
def index():
   return redirect('/login')

@modulo1.route('/login', methods=['GET', 'POST'])
def doLogin():
   if current_user.is_authenticated:
      print("Noice")

   form = UserLoginForm()
   
   if request.method == 'POST':
      print(form.login.data)
      print(form.toRegist.data)

      if form.validate_on_submit() and form.login.data == True:
         user = db.session.query(User).filter(User.student_number == form.student_number.data).first()
         if(user.password == form.password.data):
            try:
               login_user(user)
               return redirect('/homePage')
            except:
               return 'error'
               
         else:
            form.password.errors.append("Incorrenct Password")
      

      elif form.toRegist.data == True:
         return redirect('/registar')

   
   return render_template("login.html", title="Login", formFront=form)

@modulo1.route('/logout')
def logout():
   logout_user()
   return redirect(url_for('doLogin')) 