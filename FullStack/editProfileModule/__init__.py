from flask import Blueprint, request
from flask import redirect, render_template, url_for
from forms import EditUserForm
from models import User, db
from flask_login import login_user, logout_user, current_user

editProfileModule = Blueprint('editProfileModule', __name__)

@editProfileModule.route('/editProfile', methods=['GET', 'POST'])
def home():
   activeUser = current_user
   editUserForm = EditUserForm()
   if current_user.is_authenticated:
      print("Noice")
      userData = db.session.query(User).filter(User.id == activeUser.id).first()

      print(request.method)
      if(request.method == 'GET'):   
         print(str(userData.id) + " " + userData.name + " " + str(userData.phone_number) + " " + userData.password) 
         print(editUserForm.username)
         print(editUserForm.phone_number)
         
         return render_template("editorPerfil.html", title="Editar Perfil", frontEditUserForm = editUserForm, FrontUserData = userData)
        
      elif(request.method == 'POST'):
         if editUserForm.data['goBack']:
            return redirect('verPerfilPage')

         if editUserForm.validate_on_submit():
            try:
               if request.form['username'] != '':
                  userData.name = editUserForm.data['username'] 
               
               if request.form['phone_number'] != '':
                  userData.phone_number =  editUserForm.data['phone_number']

               if request.form['currentPsassword'] != '' and request.form['password'] != '' and request.form['confirm_password'] != '' :
                  if(userData.password != request.form['currentPsassword']):
                     editUserForm.currentPsassword.errors.append("Incorrect Password")
                  print(request.form['currentPsassword']  + " " + request.form['password']  + " " + request.form['confirm_password'])
                  userData.password = editUserForm.data['confirm_password']

               if request.form['user_gender'] != '':
                  userData.gender = editUserForm.data['user_gender']

               db.session.commit()
               return render_template("editorPerfil.html", title="Editar Perfil", frontEditUserForm = editUserForm, FrontUserData = userData)

            except:
               print("error")
               return render_template("editorPerfil.html", title="Editar Perfil", frontEditUserForm = editUserForm, FrontUserData = userData)
        
         
         
         
   else:
      print("Not Noice")

   return render_template("editorPerfil.html", title="Editar Perfil", frontEditUserForm = editUserForm, FrontUserData = userData)



#  username 
#     phone_number
#     password 
#     user_gender