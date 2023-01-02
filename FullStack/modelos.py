from flask_sqlalchemy import SQLAlchemy, backref
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from flask_security import (RoleMixin, UserMixin)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rides.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

roles_users_table = db.Table(
	"role_user",
	db.Column("user_id", db.Integer(), db.ForeignKey("user.id")),
	db.Column("role_id", db.Integer(), db.ForeignKey("role.id")),
)

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(255), unique=True)
	password = db.Column(db.Unicode(80))
	active = db.Column(db.Boolean())
	roles = db.relationship(
		"Role", secondary=roles_users_table, backref="user", lazy=True
	)
	
	def __str__(self):
		return self.email
	
	def has_role(self, role):
		query = db.session.query(Role).filter(Role.name == role).first()
		if query:
			if query.name in self.roles:
				return True
		return False
	
class Role(db.Model, RoleMixin):
	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(80), unique=True)
	description = db.Column(db.String(255))
	
	def __str__(self):
		return self.name

	
class Profile(db.Model): 
	__tablename__ = 'profile'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column('user_id', db.ForeignKey('user.id'), unique=True) 
	user = db.relationship('User', backref='profile')
	first_name = db.Column(db.String(30))
	last_name = db.Column(db.String(30))
	registration_date = db.Column(db.DateTime, default=datetime.now)
	photo = db.Column(db.String(60), unique=True)
	phone_number = db.Column(db.String(30), unique=True)
	smoking = db.Column(db.Boolean, default=False)
	snacking = db.Column(db.Boolean, default=False)
	drinking = db.Column(db.Boolean, default=False)
	music = db.Column(db.Boolean, default=False)
	talking = db.Column(db.Boolean, default=False)
	
	
class Vehicle(db.Model): 
	__tablename__ = 'vehicle' 
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column('user_id', db.ForeignKey('user.id')) 
	user = db.relationship('User', backref='vehicle')
	license_plate = db.Column(db.String(20), unique=True)
	vehicle_specs = db.Column(db.String(200))
	color = db.Column(db.String(20))
	is_deleted = db.Column(db.Boolean, default=False)
	createdAt = db.Column(db.DateTime, default=datetime.now)
	updatedAt = db.Column(db.DateTime, default=datetime.now)


class Local(db.Model): 
	__tablename__ = 'local'
	id =  db.Column(db.Integer, primary_key=True)
	user_id = db.Column('user_id', db.ForeignKey('user.id')) 
	user = db.relationship('User', backref='local')
	name = db.Column(db.String(100))
	description = db.Column(db.String(150))
	postal_code = db.Column(db.String(20))
	latitude = db.Column(db.Float)
	longitude = db.Column(db.Float)
	createdAt = db.Column(db.DateTime, default=datetime.now)
	updatedAt = db.Column(db.DateTime, default=datetime.now)


class Ride(db.Model): 
	__tablename__ = 'ride' 
	__table_args__ = (db.UniqueConstraint('user_id', 'vehicle_id', 'ride_date'),)
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column('user_id', db.ForeignKey('user.id')) 
	user = db.relationship('User', backref='ride')
	vehicle_id = db.Column('vehicle_id', db.ForeignKey('vehicle.id'))
	vehicle = db.relationship('Vehicle', backref='ride')
	local_id = db.Column('local_id', db.ForeignKey('local.id'))
	local = db.relationship('Local', backref='ride')
	ride_date = db.Column(db.DateTime)
	number_of_available_seats = db.Column(db.Integer())
	cost_per_passenger = db.Column(db.Float, default=0.0)
	max_waiting_time = db.Column(db.Integer(), default=5)
	is_return_trip = db.Column(db.Boolean, default=False)
	is_cancelled = db.Column(db.Boolean, default=False)
	classification = db.Column(db.Integer(), db.CheckConstraint('classification >= 1 AND classification <= 5'))
	createdAt = db.Column(db.DateTime, default=datetime.now)
	updatedAt = db.Column(db.DateTime, default=datetime.now)


class ReservationState(db.Model): 
	__tablename__ = 'reservation_state' 
	id =  db.Column(db.Integer, primary_key=True)
	state = db.Column(db.String(20))
	
	
class Reservation(db.Model):
	__tablename__ = 'reservation' 
	__table_args__ = (db.UniqueConstraint('user_id', 'ride_id'),)
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column('user_id', db.ForeignKey('user.id'))
	user = db.relationship('User', backref='reservation')
	ride_id = db.Column('ride_id', db.ForeignKey('ride.id'))
	ride = db.relationship('Ride', backref='reservation')
	local_id = db.Column('local_id', db.ForeignKey('local.id'))
	local = db.relationship('Local', backref='reservation')
	reservation_state_id = db.Column('reservation_state_id', db.ForeignKey('reservation_state.id'), default=1)
	reservation_state = db.relationship('ReservationState', backref='reservation')
	answer_date = db.Column(db.DateTime)
	classification = db.Column(db.Integer(), db.CheckConstraint('classification >= 1 AND classification <= 5'))
	createdAt = db.Column(db.DateTime, default=datetime.now)
	updatedAt = db.Column(db.DateTime, default=datetime.now)

if __name__ == "__main__":
    app.run(debug=True)
    db.create_all()