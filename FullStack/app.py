from flask import Flask
from flask_login import LoginManager
from models import db

from loginModule import loginModule
from registerModule import registerModule
from rideandreservation import rideandreservation
from homeModule import homeModule
from verPerfilModule import verPerfilModule
from editProfileModule import editProfileModule
from addVehicleModule import addVehicleModule
from rides import rides

from models import User

def create_app(config_filename):
	app = Flask(__name__)
	app.config.from_object(config_filename)
	
	db.init_app(app)

	with app.app_context():
		db.create_all()

	login_manager = LoginManager()
	login_manager.login_view = 'auth.login'
	login_manager.init_app(app)

	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(int(user_id))
	
	app.register_blueprint(loginModule)
	app.register_blueprint(registerModule)
	app.register_blueprint(rideandreservation)
	app.register_blueprint(homeModule)
	app.register_blueprint(verPerfilModule)
	app.register_blueprint(editProfileModule)
	app.register_blueprint(addVehicleModule)
	app.register_blueprint(rides)
	
	return app


if __name__ == "__main__":
	app = create_app("config.DevelopmentConfig")
	app.run()




