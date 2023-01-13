from flask import Flask
from flask_login import LoginManager
from models import db, Admin

from login import login

   
def create_app(config_filename):
    run = Flask(__name__)
    run.config.from_object(config_filename)

    db.init_app(run)

    with run.app_context():
        db.create_all()
       

    run.register_blueprint(login)

    return run


if __name__ == "__main__":
    app = create_app("config.DevelopmentConfig")
    app.run()
