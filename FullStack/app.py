from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("Login/LogIn.html")

if __name__ == "__main__":
    app.run(debug=True) 