from flask import Blueprint, flash, request
from flask import redirect, render_template, url_for
from flask_jwt_extended import JWTManager, create_access_token
from forms import UserLoginForm, ForgotPassForm
from models import User, db, bcrypt, Vehicle,Ride,Reservation, ReservationState, mail
from flask_login import login_user, logout_user, current_user
from datetime import datetime, timedelta
from flask_mail import Message

loginModule = Blueprint('loginModule', __name__)
jwtMang = JWTManager()


@loginModule.route('/')
def index():
   return redirect('/login')

# rota para realizar o login
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

# rota para realizar o logout
@loginModule.route('/logout')
def logOut():
   logout_user()
   return redirect('login')

# rota para enviar pedido de redefinir password para email de estudante
@loginModule.route('/redefinePass', methods=['GET', 'POST'])
def doRedefinePass():
   form = ForgotPassForm()

   if request.method == 'POST':

      if form.validate_on_submit() and form.sendMail.data == True:
         user = db.session.query(User).filter(User.student_number == form.student_number.data).first()

         if(user==None):
            form.student_number.errors.append("Student Number does not exist")
         else:
            make_token(user)
            flash('Email de Redifinição de Password Enviado para' + form.student_number.data + '@mso365.ismat.pt')
            return redirect(url_for('loginModule.doLogin'))
      elif form.toLogin.data == True:
         return redirect('login')


   return render_template("forgotPass.html", title="Login", formFront=form)


def send_email(subject, sender, recipients, text_body, html_body):
   msg = Message(subject, sender=sender, recipients=recipients)
   msg.body = text_body
   msg.html = html_body

      

def make_token(user):
   expires = timedelta(minutes=10)
   print(expires)
   reset_token = create_access_token(str(user.id), expires_delta=expires)
   print(reset_token)
   print(user.student_number + '@mso365.ismat.pt')

   return send_email('Reset Your Password',
                     sender='ismatridesapp@gmail.com',
                     recipients=[user.student_number + '@mso365.ismat.pt'],
                     text_body=render_template('newPass.html', url= request.host_url + 'newPass/' + reset_token),
                     html_body=render_template('newPass.html', url= request.host_url + 'newPass/' + reset_token))


@loginModule.route('/newPass')
def newpass():

   return render_template("newPass.html", title="Redifinir Password")