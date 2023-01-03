from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime
from flask_security import (RoleMixin, UserMixin)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rides.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
	
class UserRideRole(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(40), unique=True) 
	
	def __repr__(self) -> str:
		return f"UserRole('{self.name})'"
	
# class User(db.Model, UserMixin): 
# 	__tablename__ = 'profile'
# 	id = db.Column(db.Integer, primary_key=True)
# 	name = db.Column(db.String(80))
# 	student_number = db.Column(db.Integer(), unique=True)
# 	phone_number = db.Column(db.Integer(), unique=True)
# 	registration_date = db.Column(db.DateTime, default=datetime.now)
# 	password = db.Column(db.Unicode(30))
# 	gender = db.Column(db.String(80))
# 	active = db.Column(db.Boolean())

# 	def __repr__(self) -> str:
# 		return '<User %r>' % self.id

	
# class Vehicle(db.Model): 
# 	__tablename__ = 'vehicle' 
# 	id = db.Column(db.Integer, primary_key=True)
# 	owner_id = db.Column('user_id', db.ForeignKey('user.id')) 
# 	license_plate = db.Column(db.String(8), unique=True)
# 	color = db.Column(db.String(20))
# 	number_of_seats = db.Column(db.Integer())
# 	vehicle_specs = db.Column(db.String(200))
# 	is_deleted = db.Column(db.Boolean, default=False)
# 	createdAt = db.Column(db.DateTime, default=datetime.now)
# 	updatedAt = db.Column(db.DateTime, default=datetime.now)

# 	def __repr__(self) -> str:
# 		return '<User %r>' % self.id

# class Ride(db.Model): 
# 	__tablename__ = 'ride' 
# 	__table_args__ = (db.UniqueConstraint('user_id', 'vehicle_id', 'ride_date'),)
# 	id = db.Column(db.Integer, primary_key=True)
# 	user_id = db.Column('user_id', db.ForeignKey('user.id')) 
# 	user = db.relationship('User', backref='ride')
# 	vehicle_id = db.Column('vehicle_id', db.ForeignKey('vehicle.id'))
# 	ride_date = db.Column(db.DateTime)
# 	ride_scheduled_time = db.Column(db.DateTime)
# 	local_destiny = db.relationship('Local', backref='ride')
# 	local_origin = db.relationship('Local', backref='ride')
# 	number_of_available_seats = db.Column(db.Integer())	
# 	createdAt = db.Column(db.DateTime, default=datetime.now)
# 	updatedAt = db.Column(db.DateTime, default=datetime.now)

# 	def __repr__(self) -> str:
# 		return '<User %r>' % self.id

# class ReservationState(db.Model): 
# 	__tablename__ = 'reservation_state' 
# 	id =  db.Column(db.Integer, primary_key=True)
# 	state = db.Column(db.String(20)) #se boleia esta em progresso, espera, cancelada
	
	
	
# class Reservation(db.Model):
# 	__tablename__ = 'reservation' 
# 	__table_args__ = (db.UniqueConstraint('user_id', 'ride_id'),)
# 	id = db.Column(db.Integer, primary_key=True)
# 	passenger_id = db.Column('user_id', db.ForeignKey('user.id'))
# 	passenger = db.relationship('User', backref='reservation')
# 	ride_id = db.Column('ride_id', db.ForeignKey('ride.id'))
# 	ride = db.relationship('Ride', backref='reservation')
# 	reservation_state_id = db.Column('reservation_state_id', db.ForeignKey('reservation_state.id'), default=1)
# 	reservation_state = db.relationship('ReservationState', backref='reservation')
# 	createdAt = db.Column(db.DateTime, default=datetime.now)
# 	updatedAt = db.Column(db.DateTime, default=datetime.now)

# 	def __repr__(self) -> str:
# 		return '<User %r>' % self.id
		
with app.app_context():
    db.create_all()
	# useRideRole1 = UserRideRole(1, 'Condutor')
	# useRideRole2 = UserRideRole(2, 'Passageiro')

	# db.session.add(useRideRole1)
	# db.session.add(useRideRole2)
	# db.session.commit()
	
# if __name__ == "__main__":
#     app.run(debug=True)
