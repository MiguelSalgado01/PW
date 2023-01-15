from flask import Flask
from flask_login import LoginManager
from models import db, Admin

from login import login_module
from userModule import userModule
from homeModule import homeModule
from boleiasModule import rideModule


def create_app(config_filename):
    
    run = Flask(__name__)
    run.config.from_object(config_filename)

    db.init_app(run)

    with run.app_context():
        db.create_all()
        #Admin.__table__.drop()

    run.register_blueprint(login_module)
    run.register_blueprint(homeModule)
    run.register_blueprint(userModule)
    run.register_blueprint(rideModule)

    return run


if __name__ == "__main__":
    app = create_app("config.DevelopmentConfig")
    app.run(debug=True)
