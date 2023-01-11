from flask import Flask
from models import db
# from flask_login import LoginManager

from modulo1 import modulo1
from modulo2 import modulo2
from modulo3 import modulo3
from homeModule import homeModule

def create_app(config_filename):
	app = Flask(__name__)
	app.config.from_object(config_filename)
	
	db.init_app(app)

	with app.app_context():
		db.create_all()

	# login_manager.init_app(app)
	
	app.register_blueprint(modulo1)
	app.register_blueprint(modulo2)
	app.register_blueprint(modulo3)
	app.register_blueprint(homeModule)
	
	return app


if __name__ == "__main__":
	# login_manager = LoginManager()
	app = create_app("config.DevelopmentConfig")
	app.run()
	
	