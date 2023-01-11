from flask import Blueprint, request
from flask import redirect, render_template, url_for
from forms import UserLoginForm
from models import User, db

modulo1 = Blueprint('modulo1', __name__)

@modulo1.route('/')
def index():
   return redirect('/login')

@modulo1.route('/login', methods=['GET', 'POST'])
def doLogin():
   form = UserLoginForm()
   
   if request.method == 'POST':
      print(form.login.data)
      print(form.toRegist.data)

      if form.validate_on_submit() and form.login.data == True:
         verifyStudentNumb = db.session.query(User).filter(User.student_number == form.student_number.data).first()
         if(verifyStudentNumb.password == form.password.data):
            try:
               return redirect('/homePage')
            except:
               return 'error'
               
         else:
            form.password.errors.append("Incorrenct Password")
      

      elif form.toRegist.data == True:
         return redirect('/registar')

   
   return render_template("login.html", title="Login", formFront=form)
