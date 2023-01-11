from flask import Blueprint, request
from flask import redirect, render_template, url_for
from forms import UserRegisterForm
from models import User, db

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
        return render_template("registarUser.html", title="Registar User", form=form)
       

    # queryP1 = db.session.query(User).filter(User.student_number == "a32432155").first()
    # print(queryP1)


###################################################

 # print(db.session.query(User).filter_by(User.student_number == "a2434235245").first())
    # user = db.one_or_404(db.select(User).filter_by(name="a2434235245"))
    # print(user)
    # form = models.UserRegisterForm()
    # user = User.query.filter_by(student_number='a32534634')
    # user = User.query.all()
    # print(user)

    # if form.is_submitted():
        # print(form.student_number.data)
        # print(db.session.query(User).filter(User.student_number == form.student_number.data).all())
        
        # print(User.query.filter_by(student_number=form.student_number.data))
        # queryP1 = db.session.query(User).filter(User.student_number == form.student_number.data)
        # print(queryP1 == None)

        # if(queryP1 == None):
        #     return redirect(url_for('doLogin'))

        # sql = 'select * from user where user.student_number = ' + form.student_number.data
        # queryP1 = db.session.execute(sql).first()
        # print(queryP1)

    # return render_template("registarUser.html", title="Registar User", form=form)
    

#######################################################################
 
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
    


###########################################################################


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