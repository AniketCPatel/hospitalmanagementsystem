from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

class LoginForm(FlaskForm):
	username = StringField("User ID", validators=[DataRequired(), Length(min=8)])
	password = PasswordField("Password", validators=[DataRequired(), Length(min=10, max=10)])
	submit = SubmitField("Login")

	def validate_username(self, username):
		special = False
		for ch in self.username.data:
			if not ch.isalnum():
				special = True
		if special:
			raise ValidationError("Special Characters not allowed!!!")

	def validate_password(self, password):
		upper = False
		digit = False
		special = False
		for ch in self.password.data:
			if ch.isupper():
				upper = True
			if ch.isdigit():
				digit = True
			if ch.isalnum():
				special = True
		if not upper:
			raise ValidationError("Password should contain atleast 1 upper case alphabet!!!")
		if not digit:
			raise ValidationError("Password should contain atleast 1 digit!!!")
		if not special:
			raise ValidationError("Password should contain atleast 1 special character!!!")