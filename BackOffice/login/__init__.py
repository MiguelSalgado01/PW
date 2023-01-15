from flask import Blueprint,request
from flask import redirect, render_template, url_for
from forms import AdminForm
from models import db , Admin,User
from datetime import datetime

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
        if form.validate_on_submit() and form.login.data == True:
            user = db.session.query(User).filter(User.student_number == form.student_number.data).first()
            admin_id = db.session.query(Admin).filter(Admin.user_id == user.id).first()
           
            if (admin_id == None):
                 form.student_number.errors.append("Incorrect Student Number")
            else:
                 if(user.password == form.password.data):
                    #try:
                        user.active = True
                        user.last_login_date = datetime.now()
                        db.session.commit()
                        return redirect('usersPage')
                    #except:
                        # return 'error'
                 else:
                    form.password.errors.append("Incorrect Password")
    
    return render_template("pages-sign-in.html", title="Login", formFront=form)



