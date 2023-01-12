from flask import Blueprint
from flask import redirect, render_template, url_for
from forms import UserLoginForm
from models import db , Admin

login = Blueprint('login', __name__)

@login.route('/' , methods=['GET','POST'])
def index():
<<<<<<< HEAD
    return render_template("pages-sign-in.html")
=======
    #add_admin('1')
    #admin =  db.session.query(Admin).filter(Admin.id == '1').first()
    #db.session.delete(admin)
    #db.session.commit()
    #print(admin)
    return render_template("pages-sign-in.html")

def add_admin(id_user):
    new_admin = Admin(user_id = id_user)
    db.session.add(new_admin)
    db.session.commit()   


>>>>>>> c6536eeca5c410a2fa59ab63b0974dd3a76d9458

