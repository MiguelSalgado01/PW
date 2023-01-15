from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin , login_user, LoginManager, login_required,logout_user,current_user


db = SQLAlchemy()
	
class UserRideRole(db.Model):
	__tablename__ = 'user_ride_role'
	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(40), unique=True) 

	def __repr__(self) -> str:
		return f"UserRole('{self.name}')"
	
class User(db.Model):
	__tablename__ = 'user' 
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), unique=True, nullable=False)
	student_number = db.Column(db.String(9), unique=True, nullable=False)
	phone_number = db.Column(db.Integer(), nullable=False)
	password = db.Column(db.Unicode(30), nullable=False)
	gender = db.Column(db.String(10), nullable=False)
	registration_date = db.Column(db.DateTime, default=datetime.now)
	last_login_date = db.Column(db.DateTime, default=datetime.now)
	active = db.Column(db.Boolean())  

	def __repr__(self) -> str:
		return f"User('{self.name}','{self.student_number}','{self.phone_number}',{self.password}','{self.gender}','{self.registration_date}')"

	
class Vehicle(db.Model): 
	__tablename__ = 'vehicle' 
	id = db.Column(db.Integer, primary_key=True)
	owner_id = db.Column('owner_id', db.ForeignKey('user.id'), nullable=False) 
	owner = db.relationship('User', backref='vehicle')
	license_plate = db.Column(db.String(8), unique=True, nullable=False)
	color = db.Column(db.String(20), nullable=False)
	number_of_seats = db.Column(db.Integer(), nullable=False)
	vehicle_specs = db.Column(db.String(200), nullable=True)
	is_deleted = db.Column(db.Boolean, default=False)
	createdAt = db.Column(db.DateTime, default=datetime.now)
	updatedAt = db.Column(db.DateTime, default=datetime.now)

	def __repr__(self) -> str:
		return f"vehicle('{self.license_plate}','{self.color}','{self.owner_id}')"

class Ride(db.Model): 
	__tablename__ = 'ride' 
	__table_args__ = (db.UniqueConstraint('user_id', 'vehicle_id', 'ride_date'),)
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column('user_id', db.ForeignKey('user.id'), nullable=False) 
	user = db.relationship('User', backref='ride')
	vehicle_id = db.Column('vehicle_id', db.ForeignKey('vehicle.id'), nullable=False)
	vehicle = db.relationship('Vehicle', backref='ride')
	ride_date = db.Column(db.DateTime, nullable=False)
	ride_scheduled_time = db.Column(db.DateTime, nullable=False)
	local_destiny = db.Column(db.String(40), nullable=False)
	local_origin = db.Column(db.String(40), nullable=False)
	number_of_available_seats = db.Column(db.Integer(), nullable=False)	
	createdAt = db.Column(db.DateTime, default=datetime.now)
	updatedAt = db.Column(db.DateTime, default=datetime.now)

	def __repr__(self) -> str:
		return '<User %r>' % self.id

class ReservationState(db.Model): 
	__tablename__ = 'reservation_state' 
	id =  db.Column(db.Integer, primary_key=True)
	state = db.Column(db.String(20), nullable=False) #se boleia esta em progresso, espera, cancelada
	
	
	
class Reservation(db.Model):
	__tablename__ = 'reservation' 
	__table_args__ = (db.UniqueConstraint('passenger_id', 'ride_id'),)
	id = db.Column(db.Integer, primary_key=True)
	passenger_id = db.Column('passenger_id', db.ForeignKey('user.id'), nullable=False)
	passenger = db.relationship('User', backref='reservation')
	ride_id = db.Column('ride_id', db.ForeignKey('ride.id'), nullable=False)
	ride = db.relationship('Ride', backref='reservation')
	reservation_state_id = db.Column('reservation_state_id', db.ForeignKey('reservation_state.id'), default=1, nullable=False)
	reservation_state = db.relationship('ReservationState', backref='reservation')
	createdAt = db.Column(db.DateTime, default=datetime.now)
	updatedAt = db.Column(db.DateTime, default=datetime.now)

	def __repr__(self) -> str:
		return '<User %r>' % self.id


class Admin (db.Model,UserMixin ):
    __tablename__= 'Admin'
    id =  db.Column(db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='Admin')
    
    
    def __repr__(self) -> str:
        return '<Admin %r>' % self.id  
     
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_bcrypt import Bcrypt
	
db = SQLAlchemy()
bcrypt = Bcrypt()
	
class UserRideRole(db.Model):
	__tablename__ = 'user_ride_role'
	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(40), unique=True) 

	def __repr__(self) -> str:
		return f"UserRole('{self.name}')"
	
class User(db.Model, UserMixin):
	__tablename__ = 'user' 
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), unique=True, nullable=False)
	student_number = db.Column(db.String(9), unique=True, nullable=False)
	phone_number = db.Column(db.Integer(), nullable=False)
	password = db.Column(db.String(60), nullable=False)
	gender = db.Column(db.String(10), nullable=False)
	registration_date = db.Column(db.DateTime, default=datetime.now)
	last_login_date = db.Column(db.DateTime, default=datetime.now)
	active = db.Column(db.Boolean())  

	def __repr__(self) -> str:
		return f"User('{self.name}','{self.student_number}','{self.phone_number}',{self.password}','{self.gender}','{self.registration_date}')"

	
class Vehicle(db.Model): 
	__tablename__ = 'vehicle' 
	id = db.Column(db.Integer, primary_key=True)
	owner_id = db.Column('owner_id', db.ForeignKey('user.id'), nullable=False) 
	owner = db.relationship('User', backref='vehicle')
	license_plate = db.Column(db.String(8), unique=True, nullable=False)
	color = db.Column(db.String(20), nullable=False)
	number_of_seats = db.Column(db.Integer(), nullable=False)
	vehicle_specs = db.Column(db.String(200), nullable=True)
	is_deleted = db.Column(db.Boolean, default=False)
	createdAt = db.Column(db.DateTime, default=datetime.now)
	updatedAt = db.Column(db.DateTime, default=datetime.now)

	def __repr__(self) -> str:
		return f"vehicle('{self.license_plate}','{self.color}','{self.owner_id}')"

class Ride(db.Model): 
	__tablename__ = 'ride' 
	__table_args__ = (db.UniqueConstraint('user_id', 'vehicle_id', 'ride_date'),)
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column('user_id', db.ForeignKey('user.id'), nullable=False) 
	user = db.relationship('User', backref='ride')
	vehicle_id = db.Column('vehicle_id', db.ForeignKey('vehicle.id'), nullable=False)
	vehicle = db.relationship('Vehicle', backref='ride')
	ride_date = db.Column(db.String(9), nullable=False)
	ride_scheduled_time = db.Column(db.String(5), nullable=False)
	local_destiny = db.Column(db.String(40), nullable=False)
	local_origin = db.Column(db.String(40), nullable=False)
	number_of_available_seats = db.Column(db.Integer(), nullable=False)	
	createdAt = db.Column(db.DateTime, default=datetime.now)
	updatedAt = db.Column(db.DateTime, default=datetime.now)

	def __repr__(self) -> str:
		return f"Ride('{self.user_id}','{self.vehicle_id}','{self.ride_date}',{self.ride_scheduled_time}','{self.local_destiny}','{self.local_origin}','{self.number_of_available_seats}')"

class ReservationState(db.Model): 
	__tablename__ = 'reservation_state' 
	id =  db.Column(db.Integer, primary_key=True)
	state = db.Column(db.String(20), nullable=False) #se boleia esta em progresso, espera, cancelada
	def __repr__(self) -> str:
		return f"State('{self.id}','{self.state}')"

	
	
class Reservation(db.Model):
	__tablename__ = 'reservation' 
	__table_args__ = (db.UniqueConstraint('passenger_id', 'ride_id'),)
	id = db.Column(db.Integer, primary_key=True)
	passenger_id = db.Column('passenger_id', db.ForeignKey('user.id'), nullable=False)
	passenger = db.relationship('User', backref='reservation')
	ride_id = db.Column('ride_id', db.ForeignKey('ride.id'), nullable=False)
	ride = db.relationship('Ride', backref='reservation')
	reservation_state_id = db.Column('reservation_state_id', db.ForeignKey('reservation_state.id'), default=1, nullable=False)
	reservation_state = db.relationship('ReservationState', backref='reservation')
	createdAt = db.Column(db.DateTime, default=datetime.now)
	updatedAt = db.Column(db.DateTime, default=datetime.now)

	def __repr__(self) -> str:
		return f"Reservation('{self.id}','{self.passenger_id}','{self.ride_id}')"









