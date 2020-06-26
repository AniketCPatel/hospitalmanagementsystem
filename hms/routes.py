from hms import app, db, bcrypt
from hms.forms import LoginForm, SearchForm
from hms.models import User, Patient
from flask import render_template, redirect, url_for, session, flash, request


@app.route('/', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			password = bcrypt.check_password_hash(user.password, form.password.data)
			if password:
				session['USER_ID'] = user.username
				session['ROLE'] = user.role
				flash("Successfully Logged In", category="success")
				return redirect(url_for('login'))
			else:
				flash("Wrong password entered!!!", category="danger")
		else:
			flash("Wrong username entered!!!", category="danger")		
	return render_template('login.html', title='Login', form=form)


@app.route('/view_active_patients')
def view_active_patients():
	if session.get('ROLE') != "adm_desk":
		flash("Action Forbidden!!!", category="danger")
		return redirect(url_for('login'))
	else:
		page = request.args.get('page', 1, type=int)
		patients = Patient.query.filter_by(patient_status="active").order_by(Patient.patient_id).paginate(page=page, per_page=10)
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
			return render_template('show_patient_details.html', title="Patient Details", patient=patient)


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


@app.route('/logout')
def logout():
	session['USER_ID'] = None
	flash("Successfully Logged Out", category="success")
	return redirect(url_for('login'))