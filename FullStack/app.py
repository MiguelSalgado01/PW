from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("LogIn.html")
    
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

@app.route('/login')
def login():
    return render_template("logIn.html")

@app.route('/novaPassword')
def newPass():
    return render_template("newPass.html")

@app.route('/novoVeiculo')
def registarVeic():
    return render_template("registarVeiculo.html")

@app.route('/registar')
def registarUser():
    return render_template("register.html")

@app.route('/reservas')
def abrirReservas():
    return render_template("reservas.html")
    
@app.route('/pesquisa')
def pesquisarBoleias():
    return render_template("pesquisa.html")
    

if __name__ == "__main__":
    app.run(debug=True) 