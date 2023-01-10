from flask import Blueprint
from flask import redirect, render_template, url_for
from forms import UserRegisterForm

modulo2 = Blueprint('modulo2', __name__)

@modulo2.route('/registar', methods=['GET', 'POST'])
def register():
    form = UserRegisterForm()

    if form.validate_on_submit():
        return redirect('/login')
        
    return render_template("registarUser.html", title="Registar User", form=form)
