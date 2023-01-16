from flask import Blueprint, request
from flask import redirect, render_template, url_for
from forms import EditUserForm
from models import User, db, bcrypt
from flask_login import current_user

editProfileModule = Blueprint('editProfileModule', __name__)

@editProfileModule.route('/editProfile', methods=['GET', 'POST'])
def home():
   activeUser = current_user
   editUserForm = EditUserForm()
   if current_user.is_authenticated:
      userData = db.session.query(User).filter(User.id == activeUser.id).first()

      if(request.method == 'GET'):   
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
               
               if(request.form['currentPassword'] != ''):  
                  if bcrypt.check_password_hash(userData.password, request.form['currentPassword']) == True:
                     if request.form['password'] != '' and request.form['confirm_password'] != '' :

                        if(len(request.form['password']) < 8 or len(request.form['password']) > 20):
                           editUserForm.password.errors.append("Field must be between 8 and 20 characters long")

                        elif(len(request.form['confirm_password']) < 8 or len(request.form['confirm_password']) > 20):
                           editUserForm.password.errors.append("Field must be between 8 and 20 characters long")
                        
                        elif(request.form['password'] == request.form['confirm_password']):
                           encrypted_password = bcrypt.generate_password_hash(request.form['confirm_password']).decode('UTF-8')
                           userData.password = encrypted_password

                     else:
                        editUserForm.password.errors.append("Field must be filled")
                        editUserForm.confirm_password.errors.append("Field must be filled")

                  elif(bcrypt.check_password_hash(userData.password, request.form['currentPassword']) != True):
                     editUserForm.currentPassword.errors.append("Incorrect Password")

               if request.form['user_gender'] != '':
                  userData.gender = editUserForm.data['user_gender']

               db.session.commit()
               return render_template("editorPerfil.html", title="Editar Perfil", frontEditUserForm = editUserForm, FrontUserData = userData)

            except:
               print("erro")
               return render_template("editorPerfil.html", title="Editar Perfil", frontEditUserForm = editUserForm, FrontUserData = userData)
        
         return render_template("editorPerfil.html", title="Editar Perfil", frontEditUserForm = editUserForm, FrontUserData = userData)
      
   else:
      print("Not Noice")

   return render_template("editorPerfil.html", title="Editar Perfil", frontEditUserForm = editUserForm, FrontUserData = userData)