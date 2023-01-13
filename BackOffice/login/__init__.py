from flask import Blueprint,request
from flask import redirect, render_template, url_for
from forms import AdminForm
from models import db , Admin

login = Blueprint('login', __name__)

@login.route('/')
def index():
    return redirect('/pages-sign-in')

@login.route('/pages-sign-in', methods=['GET', 'POST'])
def doLogin():
    form = AdminForm()
    
    
    admin =  db.session.query(Admin).filter(Admin.student_number == 'a22007528').first()
    db.session.commit()
    print(admin)
         
    if request.method == 'POST':
      print(form.login.data)
      
    if form.validate_on_submit() and form.login.data == True:
        verifyStudentNumb = db.session.query(Admin).filter(Admin.student_number == form.student_number.data).first()
        if(verifyStudentNumb.password == form.password.data):
            try:
               return render_template ('index.html')
            except:
               return 'error'
           
        else:
            form.password.errors.append("Incorrenct Password")
    
      

    return render_template("pages-sign-in.html", title="Login", formFront=form)
  
  

  
  
'''
def add_admin(id_user):
    new_admin = Admin(user_id = id_user)
    db.session.add(new_admin)
    db.session.commit()   
'''


