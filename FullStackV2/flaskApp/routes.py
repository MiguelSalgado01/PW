from flaskApp import app
from flask import redirect, render_template, url_for
from flaskApp.forms import UserRegisterForm
 
@app.route('/', methods=['GET'])
def index():
    return render_template("logIn.html")
#    return redirect('/registar')

# @app.route('/login', methods=['GET', 'POST'])
# def doLogin():
#     return render_template("logIn.html")

# @app.route('/registar', methods=['GET', 'POST'])
# def register():
#     form = UserRegisterForm()

#     if form.validate_on_submit():
#         return redirect(url_for('doLogin'))
        
#     return render_template("registarUser.html", title="Registar User", form=form)
