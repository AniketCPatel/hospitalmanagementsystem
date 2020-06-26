from hms import app, db
from hms.forms import LoginForm
from hms.models import User
from flask import render_template, redirect, url_for, session, flash

@app.route('/', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user:
			if user.password == form.password.data:
				session['USER_ID'] = user.username
				session['ROLE'] = user.role
				flash("Successfully Logged In", category="success")
				return redirect(url_for('login'))
			else:
				flash("Wrong password entered!!!", category="danger")
		else:
			flash("Wrong username entered!!!", category="danger")		
	return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
	session['USER_ID'] = None
	flash("Successfully Logged Out", category="success")
	return redirect(url_for('login'))