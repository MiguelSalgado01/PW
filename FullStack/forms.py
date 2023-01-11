from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, InputRequired

class UserRegisterForm(FlaskForm):
    username = StringField(label="Nome Utilizador", validators=[InputRequired(),Length(min=6, max=30)])
    student_number = StringField(label="Numero Estudante", validators=[InputRequired(), Length(min=9, max=9)])
    phone_number = StringField(label="Contacto", validators=[InputRequired(), Length(min=9, max=9)])
    password = PasswordField(label="Password", validators=[InputRequired(),  Length(min=8, max=20)])
    confirm_password = PasswordField(label="Confirmar Password", validators=[InputRequired(), EqualTo("password")])
    user_gender =  SelectField(label="Genero", validators=[DataRequired()], choices=[(" ","Selecionar Genero"), ("0","Feminino"), ("1","Masculino")])
    submitRegist = SubmitField(label="Registar")
    toLogin = SubmitField(label="Login")

class UserLoginForm(FlaskForm):
    student_number = StringField(label="Numero Estudante", validators=[InputRequired(), Length(min=9, max=9)])
    password = PasswordField(label="Password", validators=[InputRequired(),  Length(min=8, max=20)])
    login = SubmitField(label="Login")
    toRegist = SubmitField(label="Cria Conta")
