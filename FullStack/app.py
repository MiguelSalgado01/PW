from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, render_template, request, redirect, url_for
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rides.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/', methods=['GET'])
def index():
   return redirect('/registar')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("logIn.html")

@app.route('/registar', methods=['GET', 'POST'])
def registarUser(nomeUtilizador="",numeroEstudante="",contactoUtilizador="",passEstudante="",confPassUtilizador="",genderEstudante=""):
    if request.method == 'GET': 
        return render_template("register.html")

    if request.method == 'POST': 
        nomeUtilizador = request.form.get('username', nomeUtilizador)
        numeroEstudante = request.form.get('studentNumber', numeroEstudante)
        contactoUtilizador = request.form.get('contact', contactoUtilizador)
        passEstudante = request.form.get('pass', passEstudante)
        confPassUtilizador = request.form.get('confPass', confPassUtilizador)
        genderEstudante = request.form.get('gender', genderEstudante)
        
        # print(nomeUtilizador + " " + numeroEstudante + " " +  contactoUtilizador + " " +  passEstudante + " " +  confPassUtilizador + " " +  genderEstudante )
        
        with app.app_context():
            try:
                # new_user = User(name=nomeUtilizador,student_number=numeroEstudante,phone_number=contactoUtilizador,password=passEstudante,gender=genderEstudante)
                # print(User.query.filter_by(name=nomeUtilizador))
                # print(User.query.filter_by(student_number=numeroEstudante))
                userQuery = db.one_or_404(db.select(User).filter_by(name=nomeUtilizador))
                db.session.add(new_user)
                db.session.commit()
                return userQuery
            except:
                return 'error'
        return redirect('/login')
        
    
if __name__ == "__main__":
    app.run(debug=True) 
    
# @app.route('/criarBoleia')
# def criarBoleia():
#     return render_template("criaBoleia.html")

# @app.route('/editarPerfil')
# def editarPerfil():
#     return render_template("editorPerfil.html")

# @app.route('/error')
# def erro():
#     return render_template("error.html")

# @app.route('/esqueceuPass')
# def esqueceuPass():
#     return render_template("forgotPass.html")

# @app.route('/home')
# def abrirHome():
#     return render_template("home.html")


# @app.route('/novaPassword')
# def newPass():
#     return render_template("newPass.html")

# @app.route('/novoVeiculo')
# def registarVeic():
#     return render_template("registarVeiculo.html")

# @app.route('/reservas')
# def abrirReservas():
#     return render_template("reservas.html")
    
# @app.route('/pesquisa')
# def pesquisarBoleias():
#     return render_template("pesquisa.html")
    

    # users = db.query.all()
    # print(jsonify(users))