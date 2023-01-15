from flask import Flask
from flask_login import LoginManager
from models import db, bcrypt, Admin, User


from login import login_module
from userModule import userModule
from homeModule import homeModule
from boleiasModule import rideModule
from ReservasModule import reservaModule


def create_app(config_filename):
    
    run = Flask(__name__)
    run.config.from_object(config_filename)

    db.init_app(run)
    bcrypt.init_app(run)

    with run.app_context():
        db.create_all()
        #Admin.__table__.drop()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(run)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    run.register_blueprint(login_module)
    run.register_blueprint(homeModule)
    run.register_blueprint(userModule)
    run.register_blueprint(rideModule)
    run.register_blueprint(reservaModule)

    return run


if __name__ == "__main__":
    run = create_app("config.DevelopmentConfig")
    run.run(debug=True)
