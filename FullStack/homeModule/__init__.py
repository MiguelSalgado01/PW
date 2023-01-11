from flask import Blueprint, request
from flask import redirect, render_template, url_for

homeModule = Blueprint('homeModule', __name__)

@homeModule.route('/homePage', methods=['GET', 'POST'])
def home():
   return render_template("home.html")
