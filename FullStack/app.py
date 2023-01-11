from flask import Flask
from models import db

from modulo1 import modulo1
from modulo2 import modulo2

def create_app(config_filename):
	app = Flask(__name__)
	app.config.from_object(config_filename)
	
	db.init_app(app)

	with app.app_context():
		db.create_all()
	
	app.register_blueprint(modulo1)
	app.register_blueprint(modulo2)
	
	return app


if __name__ == "__main__":
	app = create_app("config.DevelopmentConfig")
	app.run()