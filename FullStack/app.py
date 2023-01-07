from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, render_template, request, redirect, url_for
from models import db, User
from forms import UserRegisterForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rides.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']='hardsecretkey'

db.init_app(app)

@app.route('/', methods=['GET'])
def index():
   return redirect('/registar')

@app.route('/login', methods=['GET', 'POST'])
def doLogin():
    return render_template("logIn.html")

@app.route('/registar', methods=['GET', 'POST'])
def register():
    form = UserRegisterForm()
    
    if form.validate_on_submit():
        return redirect(url_for('doLogin'))

    return render_template("registarUser.html", title="Registar User", form=form)

if __name__ == "__main__":
    app.run(debug=True) 
    # users = db.query.all()
    # print(jsonify(users))
    
@app.route('/criarBoleia')
def criarBoleia():
    return render_template("criaBoleia.html")

@app.route('/editarPerfil')
def editarPerfil():
    return render_template("editorPerfil.html")

@app.route('/error')
def erro():
    return render_template("error.html")

@app.route('/esqueceuPass')
def esqueceuPass():
    return render_template("forgotPass.html")

@app.route('/home')
def abrirHome():
    return render_template("home.html")


@app.route('/novaPassword')
def newPass():
    return render_template("newPass.html")

@app.route('/novoVeiculo')
def registarVeic():
    return render_template("registarVeiculo.html")

@app.route('/reservas')
def abrirReservas():
    return render_template("reservas.html")
    
@app.route('/pesquisa')
def pesquisarBoleias():
    return render_template("pesquisa.html")
    


    # def registarUser(nomeUtilizador="",numeroEstudante="",contactoUtilizador="",passEstudante="",confPassUtilizador="",genderEstudante=""):
    # if request.method == 'GET': 
    #     return render_template("register.html")

    # if request.method == 'POST': 
    #     nomeUtilizador = request.form.get('username', nomeUtilizador)
    #     numeroEstudante = request.form.get('studentNumber', numeroEstudante)
    #     contactoUtilizador = request.form.get('contact', contactoUtilizador)
    #     passEstudante = request.form.get('pass', passEstudante)
    #     confPassUtilizador = request.form.get('confPass', confPassUtilizador)
    #     genderEstudante = request.form.get('gender', genderEstudante)
        
    #     # print(nomeUtilizador + " " + numeroEstudante + " " +  contactoUtilizador + " " +  passEstudante + " " +  confPassUtilizador + " " +  genderEstudante )
        
    #     with app.app_context():
    #         try:
    #             new_user = User(name=nomeUtilizador,student_number=numeroEstudante,phone_number=contactoUtilizador,password=passEstudante,gender=genderEstudante)
    #             # print(User.query.filter_by(name=nomeUtilizador))
    #             # print(User.query.filter_by(student_number=numeroEstudante)) 
    #             db.session.add(new_user)
    #             db.session.commit()

    #             # userQuery = db.one_or_404(db.select(User).filter_by(name=nomeUtilizador)) # 

    #             # queryP1 = db.session.query(User).filter(User.name == nomeUtilizador).first()

    #             # se username já existe queryP1 = db.session.query(User).filter(User.name == nomeUtilizador).first()
    #             # manda mensagem pro front

    #             # se studentNumb já existe queryP1 = db.session.query(User).filter(User.student_number == numeroEstudante).first()
    #             # manda mensagem pro front

    #             # se algum do campos não tiver preenchido 
    #             # manda mensagem pro front

    #             # sql = 'select * from user where user.name =' + nomeUtilizador
    #             # queryP1 = db.session.execute(sql).first()
    #             # print(queryP1)

                
    #             # return 'userQuery'
    #             return None
    #         except:
    #             return 'error'

    # return redirect('/login')