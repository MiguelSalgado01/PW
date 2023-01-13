from flask import Blueprint, request
from flask import redirect, render_template, url_for
from forms import RideForm
from models import User, db

rides = Blueprint('rides', __name__)

@rides.route('/rides', methods=['GET', 'POST'])
def doLogin():
    return render_template("criarBoleia.html")



from flask import Blueprint
from flask import redirect, render_template, url_for
from forms import UserRegisterForm

modulo2 = Blueprint('modulo2', __name__)

@modulo2.route('/registar', methods=['GET', 'POST'])
def register():
    form = UserRegisterForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            verifyStudentNumb = db.session.query(User).filter(User.student_number == form.student_number.data).first()
            verifyUsername = db.session.query(User).filter(User.name == form.username.data).first()
            if(verifyStudentNumb == None and verifyUsername == None):
                try:
                    new_user = User(name=form.username.data,student_number=form.student_number.data,phone_number=form.phone_number.data,password=form.password.data,gender=form.user_gender.data)
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
        
        elif request.form['LogBtn'] == 'Tenho Conta':
            return redirect('/login')
       
    elif request.method == 'GET': 
        return render_template("registarUser.html", title="Criar Boleia", form=form)
  