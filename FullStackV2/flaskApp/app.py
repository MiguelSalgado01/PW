from flask import Flask
from flaskApp.models import db
from yourapplication.views.admin import admin
from yourapplication.views.frontend import frontend

def create_app(config_filename):
    app = Flask(__name__)
    # app.config.from_pyfile(config_filename)

    db.init_app(app)

    app.register_blueprint(admin)
    app.register_blueprint(frontend)

    return app



# if __name__ == "__main__":
#     app.run(debug=True)	