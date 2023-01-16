from flask import Blueprint,request
from flask import redirect, render_template, url_for, jsonify
from forms import AdminForm
from models import db , Admin,User
from datetime import datetime
from flask_login import current_user

userModule = Blueprint('userModule', __name__)


@userModule.route('/usersPage', methods=['GET', 'POST'])
def toUsersPage():
    if current_user.is_authenticated:
        print("Noice")
    else:
         print("Not Noice")
    if request.method == 'GET':
        get_Users = db.session.query(User).all()
        return render_template("users.html", title="Login", get_Users = get_Users)
    elif request.method == 'POST':
        id = request.form.get("id")
        print(id)
        specify_User = db.session.query(User).filter(User.id==id).first()
        print(specify_User)
        db.session.delete(specify_User)
        db.session.commit()
        
       
    # get_Users = db.session.query(User).all()
    # # form = AdminForm()
    # return render_template("users.html", title="Login", get_Users = get_Users)
    return  jsonify(message="Apagado",status=201)



