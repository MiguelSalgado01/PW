from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, InputRequired

class UserRegisterForm(FlaskForm):
    username = StringField(label="Nome Utilizador", validators=[InputRequired(),Length(min=6, max=30)])
    student_number = StringField(label="Numero Estudante", validators=[InputRequired(), Length(min=9, max=9)])
    phone_number = StringField(label="Contacto", validators=[InputRequired(), Length(min=9, max=9)])
    password = PasswordField(label="Password", validators=[InputRequired(),  Length(min=8, max=20)])
    confirm_password = PasswordField(label="Confirmar Password", validators=[InputRequired(), EqualTo("password")])
    user_gender =  SelectField(label="Genero", validators=[DataRequired()], choices=[(" ","Selecionar Genero"), ("0","Feminino"), ("1","Masculino")])
    submitRegist = SubmitField(label="Registar")
    login = SubmitField(label="Tenho Conta")

class UserLoginForm(FlaskForm):
    student_number = StringField(label="Numero Estudante", validators=[InputRequired(), Length(min=9, max=9)])
    password = PasswordField(label="Password", validators=[InputRequired(),  Length(min=8, max=20)])
    login = SubmitField(label="Login")
    toRegist = SubmitField(label="Cria Conta")

class HomeForm(FlaskForm):
    verPerfil = SubmitField(label="Ver Perfil")
    criarBoleia = SubmitField(label="Criar Boleia")
    pesquisar = SubmitField(label="Pesquisar Boleia")
    reservas = SubmitField(label="Minhas Reservas")
    endSession = SubmitField(label="Terminar Sessão")

class ProfileForm(FlaskForm):
    goBack = SubmitField(label="Ecrã Prévio")
    editarPerfil = SubmitField(label="Editar Perfil")
    adicionarVeiculo = SubmitField(label="Associar Veiculo")

class VehicleForm(FlaskForm):
    plate = StringField(label="Matricula", validators=[InputRequired(), Length(min=8, max=8)])
    color = StringField(label="Cor", validators=[InputRequired(),  Length(min=2, max=20)])
    sits = SelectField(label="Lugares Disponiveis", validators=[DataRequired()], choices=[(" ","Selecionar Capacidade"), ("1","1"), ("2","2"), ("3","3"), ("4","4"), ("5","5"), ("6","6")])
    Specs = TextAreaField(label="Especificações", validators=[Length(max=200)])
    regist = SubmitField(label="Guardar Veiculo")
    goBack = SubmitField(label="Ecrã Prévio")
    
    
class RideForm(FlaskForm):
    vehicle = StringField(label="veiculo", validators=[InputRequired(), Length(min=9, max=9)])
    data = StringField(label="data", validators=[InputRequired(),  Length(min=8, max=20)])
    hora = StringField(label="hora", validators=[InputRequired(),  Length(min=8, max=20)])
    place = StringField(label="local", validators=[InputRequired(),  Length(min=8, max=20)])
    comGo = StringField(label="comeGo", validators=[InputRequired(),  Length(min=8, max=20)])
    comGo = StringField(label="comeGo", validators=[Length(min=8, max=20)])
    toRegist = SubmitField(label="Add Veiculo")