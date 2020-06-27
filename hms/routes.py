from hms import app, db, bcrypt
from hms.forms import LoginForm, SearchForm, PatientDetailsForm, ConfirmationForm, MedicinesForm, DiagnosticsForm
from hms.models import User, Patient, Medicine, Diagnostics
from flask import render_template, redirect, url_for, session, flash, request
from datetime import date as dt
from sqlalchemy import or_


@app.route('/', methods=['GET', 'POST'])
def login():
	if session.get('USER_ID'):
		flash("Already Logged In!!!", category="danger")
		return redirect(url_for('search_patient'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			password = bcrypt.check_password_hash(user.password, form.password.data)
			if password:
				session['USER_ID'] = user.username
				session['ROLE'] = user.role
				flash("Successfully Logged In", category="success")
				return redirect(url_for('search_patient'))
			else:
				flash("Wrong password entered!!!", category="danger")
		else:
			flash("Wrong username entered!!!", category="danger")		
	return render_template('login.html', title='Login', form=form)


@app.route('/view_active_patients')
def view_active_patients():
	if session.get('ROLE') != "adm_desk":
		flash("Action Forbidden!!!", category="danger")
		return redirect(url_for('search_patient'))
	else:
		page = request.args.get('page', 1, type=int)
		patients = Patient.query.filter_by(patient_status="Active").order_by(Patient.patient_id).paginate(page=page, per_page=10)
		return render_template('view_active_patients.html', title="All Patients", patients=patients)


@app.route('/show_patient_details')
def show_patient_details():
	patient_id = request.args.get('patient_id', None, type=int)
	if not patient_id:
		flash("Patient Not Found!!!", category="danger")
		return redirect(url_for('search_patient'))
	else:
		patient = Patient.query.filter_by(patient_id=patient_id).first()
		if not patient:
			flash("Patient Not Found!!!", category="danger")
			return redirect(url_for('search_patient'))
		else:
			med_total_amount = 0
			diag_total_amount = 0
			for medicine in patient.medicines:
				med_total_amount += medicine.medicine_amount
			for diagnostic in patient.diagnostics:
				diag_total_amount += diagnostic.diagnostics_amount
			return render_template('show_patient_details.html', title="Patient Details", patient=patient, med_total_amount=med_total_amount, diag_total_amount=diag_total_amount)


@app.route('/search_patient', methods=['GET', 'POST'])
def search_patient():
	form = SearchForm()
	if form.validate_on_submit():
		patient = Patient.query.filter_by(patient_id=form.patient_id.data).first()
		if not patient:
			flash("Patient Not Found!!!", category="danger")
			return redirect(url_for('search_patient'))
		else:
			return redirect(url_for('show_patient_details', patient_id=patient.patient_id))
	return render_template('search_patient.html', title="Search Patient", form=form)


@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
	if session.get('ROLE') != "adm_desk":
		flash("Action Forbidden!!!", category="danger")
		return redirect(url_for('search_patient'))
	else:
		form = PatientDetailsForm()
		if not form.patient_id.data:
			form.patient_id.data = PatientDetailsForm.generate_patient_id()
		form.patient_DOD.data = dt(3000,1,1)
		if form.validate_on_submit():
			patient = Patient(ssn=form.ssn.data, patient_id=form.patient_id.data, patient_name=form.patient_name.data, patient_address=form.patient_address.data, patient_age=form.patient_age.data, patient_DOJ=form.patient_DOJ.data, patient_DOD=form.patient_DOD.data, patient_room_type=form.patient_room_type.data, patient_state=form.patient_state.data, patient_city=form.patient_city.data, patient_status=form.patient_status.data)
			db.session.add(patient)
			db.session.commit()
			flash("Patient Successfully Added!!!", category="success")
			return redirect(url_for('show_patient_details', patient_id=patient.patient_id))
		return render_template('add_patient.html', title="Add Patient", form=form)


@app.route('/update_patient_details', methods=['GET', 'POST'])
def update_patient_details():
	if session.get('ROLE') != "adm_desk":
		flash("Action Forbidden!!!", category="danger")
		return redirect(url_for('search_patient'))
	else:
		form = PatientDetailsForm()
		patient_id = request.args.get('patient_id', None, type=int)
		patient = Patient.query.filter_by(patient_id=patient_id).first()
		form.ssn.data = patient.ssn
		form.patient_id.data = patient_id
		form.patient_DOJ.data = patient.patient_DOJ
		form.patient_DOD.data = patient.patient_DOD
		form.patient_status.data = patient.patient_status
		if form.validate_on_submit():
			patient.patient_name = form.patient_name.data
			patient.patient_address = form.patient_address.data
			patient.patient_age = form.patient_age.data
			patient.patient_room_type = form.patient_room_type.data
			patient.patient_state = form.patient_state.data
			patient.patient_city = form.patient_city.data
			db.session.commit()
			flash("Patient Details Successfully Updated!!!", category="success")
			return redirect(url_for('show_patient_details', patient_id=patient_id))
		return render_template('update_patient_details.html', title="Update Details", form=form, patient_id=patient_id)


@app.route('/delete_patient', methods=['GET', 'POST'])
def delete_patient():
	if session.get('ROLE') != "adm_desk":
		flash("Action Forbidden!!!", category="danger")
		return redirect(url_for('search_patient'))
	else:
		form = ConfirmationForm()
		patient_id = request.args.get('patient_id', None, type=int)
		patient = Patient.query.filter_by(patient_id=patient_id).first()
		if form.validate_on_submit():
			if form.patient_id.data == patient_id and patient_id != None:
				patient.patient_status = "Inactive"
				db.session.commit()
				flash("Patient Data Successfully Deleted!!!", category="success")
				return redirect(url_for('search_patient'))
			else:
				flash("Patient Not Found!!!", category="danger")
				return redirect(url_for('search_patient'))
		return render_template('delete_patient.html', title="Delete Patient", form=form, patient=patient)


@app.route('/issue_medicines', methods=['GET', 'POST'])
def issue_medicines():
	if session.get('ROLE') != "pharm":
		flash("Action Forbidden!!!", category="danger")
		return redirect(url_for('search_patient'))
	else:
		form = MedicinesForm()
		patient_id = request.args.get('patient_id', None, type=int)
		patient = Patient.query.filter_by(patient_id=patient_id).first()
		if not form.medicine_id.data:
			form.medicine_id.data = MedicinesForm.generate_medicine_id()
		if form.validate_on_submit() and patient_id:
			medicine_amount = (form.medicine_rate.data * form.medicine_quantity.data)
			medicine = Medicine(medicine_id=form.medicine_id.data, medicine_name=form.medicine_name.data, medicine_rate=form.medicine_rate.data, medicine_quantity=form.medicine_quantity.data, medicine_amount=medicine_amount, patient_id=patient_id)
			db.session.add(medicine)
			db.session.commit()
			flash("Medicine Successfully Added!!!", category="success")
			return redirect(url_for('show_patient_details', patient_id=medicine.patient_id))
		elif not patient_id:
			flash("Patient Not Found!!!", category="danger")
			return redirect(url_for('search_patient'))
		med_total_amount = 0
		for medicine in patient.medicines:
			med_total_amount += medicine.medicine_amount
		return render_template('issue_medicines.html', title="Add Medicines", form=form, patient=patient, med_total_amount=med_total_amount)


@app.route('/add_diagnostics_test', methods=['GET', 'POST'])
def add_diagnostics_test():
	if session.get('ROLE') != "diag":
		flash("Action Forbidden!!!", category="danger")
		return redirect(url_for('search_patient'))
	else:
		form = DiagnosticsForm()
		patient_id = request.args.get('patient_id', None, type=int)
		patient = Patient.query.filter_by(patient_id=patient_id).first()
		if not form.diagnostics_id.data:
			form.diagnostics_id.data = DiagnosticsForm.generate_diagnostics_id()
		if form.validate_on_submit() and patient_id:
			diagnostic = Diagnostics(diagnostics_id=form.diagnostics_id.data, diagnostics_name=form.diagnostics_name.data, diagnostics_amount=form.diagnostics_amount.data, patient_id=patient_id)
			db.session.add(diagnostic)
			db.session.commit()
			flash("Diagnostics Test Added Successfully!!!", category="success")
			return redirect(url_for('show_patient_details', patient_id=patient_id))
		elif not patient_id:
			flash("User Not Found!!!", category="danger")
			return redirect(url_for('search_patient'))
		diag_total_amount = 0
		for diagnostic in patient.diagnostics:
			diag_total_amount += diagnostic.diagnostics_amount
		return render_template('add_diagnostics_test.html', title="Add Diagnostics Test", form=form, patient=patient, diag_total_amount=diag_total_amount)


@app.route('/logout')
def logout():
	session['USER_ID'] = None
	flash("Successfully Logged Out", category="success")
	return redirect(url_for('login'))