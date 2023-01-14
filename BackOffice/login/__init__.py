from flask import Blueprint,request
from flask import redirect, render_template, url_for
from forms import AdminForm
from models import db , Admin,User

login_module = Blueprint('login', __name__)

@login_module.route('/')
def index():
    return redirect('/pages-sign-in')


@login_module.route('/pages-sign-in', methods=['GET', 'POST'])

def doLogin():
    # Query para Buscar all users
    get_Users = db.session.query(User).all()
    form = AdminForm()
       
    if request.method == 'POST':
      print(form.login.data)
      
          
    if form.validate_on_submit() and form.login.data == True:
        verifyStudentNumb = db.session.query(Admin).filter(Admin.student_number == form.student_number.data).first()
        
        if (verifyStudentNumb == None):
            form.student_number.errors.append("Incorrect Student Number")
        else:
            if(verifyStudentNumb.password == form.password.data):
                try:
                    return render_template ('index.html',get_Users=get_Users)
                except:
                    return 'error'
           
            else:
                form.password.errors.append("Incorrect Password")
    
    return render_template("pages-sign-in.html", title="Login", formFront=form)



