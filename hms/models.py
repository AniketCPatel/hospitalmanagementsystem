from hms import db

class User(db.Model):
	username = db.Column(db.String(20), primary_key=True)
	password = db.Column(db.String(50), nullable=False)
	role = db.Column(db.String(10), nullable=False)

class Patient(db.Model):
	ssn = db.Column(db.Integer, nullable=False)
	patient_id = db.Column(db.Integer, primaty_key=True)
	patient_name = db.Column(db.String(20), nullable=False)
	patient_address = db.Column(db.String(100), nullable=False)
	patient_age = db.Column(db.Integer, nullable=False)
	patient_DOJ = db.Column(db.Date, nullable=False)
	patient_DOD = db.Column(db.Date, nullable=True)
	patient_room_type = db.Column(db.String(10), nullable=False)
	patient_state = db.Column(db.String(20), nullable=False)
	patient_city = db.Column(db.String(20), nullable=False)
	patient_status = db.Column(db.String(10, nullable=False))
	medicines = db.relationship('Medicine', backref='patient', lazy=True)
	diagnostics = db.relationship('Diagnostics', backref='patient', lazy=True)

class Medicine(db.Model):
	medicine_name = db.Column(db.String(20), nullable=False)
	medicine_quantity = db.Column(db.Integer, nullable=False)
	medicine_rate = db.Column(db.Float, nullable=False)
	medicine_amount = db.Column(db.Float, default=(medicine_amount*medicine_rate), nullable=False)
	patient_id = db.Column(db.Integer, db.ForeignKey('patient.patient_id'), nullable=False)

class Diagnostics(db.Model):
	diagnostics_name = db.Column(db.String(20), nullable=False)
	diagnostics_amount = db.Column(db.Float, nullable=False)
	patient_id = db.Column(db.Integer, db.ForeignKey('patient.patient_id'), nullable=False)