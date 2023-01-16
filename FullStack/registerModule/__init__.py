from flask import Blueprint, request
from flask import redirect, render_template, url_for
from forms import UserRegisterForm
from models import User, db, bcrypt
from flask_login import login_user, logout_user, current_user

registerModule = Blueprint('registerModule', __name__)

@registerModule.route('/registar', methods=['GET', 'POST'])
def register():
    form = UserRegisterForm()
    
    if request.method == 'POST':
        if form.validate_on_submit() and form.submitRegist.data == True:
            verifyStudentNumb = db.session.query(User).filter(User.student_number == form.student_number.data).first()
            verifyUsername = db.session.query(User).filter(User.name == form.username.data).first()

            encrypted_password = bcrypt.generate_password_hash(form.password.data).decode('UTF-8')
            
            
            if(verifyStudentNumb == None and verifyUsername == None):
                try:
                    new_user = User(name=form.username.data,student_number=form.student_number.data,
                        phone_number=form.phone_number.data,password=encrypted_password,
                        gender=form.user_gender.data, active=True)

                    db.session.add(new_user)
                    db.session.commit()
                    return redirect('/login')
                except:
                    return 'error'
                    
            elif(verifyStudentNumb != None and verifyUsername != None):
                form.student_number.errors.append("Student number already exists")
                form.username.errors.append("Username number already exists")
            elif(verifyStudentNumb != None):
                form.student_number.errors.append("Student number already exists")
            elif(verifyUsername != None):
                form.username.errors.append("Username number already exists")
        
        elif form.login.data == True:
            return redirect('/login')
       
    elif request.method == 'GET': 
        return render_template("registarUser.html", title="Registar User", formFront=form)
       
    return render_template("registarUser.html", title="Registar User", formFront=form)