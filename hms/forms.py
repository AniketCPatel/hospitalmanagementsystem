from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, DateField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError
from datetime import date as dt
from hms.models import Patient


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

class SearchForm(FlaskForm):
	patient_id = IntegerField("Patient ID", validators=[DataRequired()])
	submit = SubmitField("Search")

	def validate_patient_id(self, patient_id):
		if patient_id.data < 10000000:
			raise ValidationError("Patient ID should be atleast 8 digits!!!")

class PatientDetailsForm(FlaskForm):
	ssn = IntegerField("SSN", validators=[DataRequired()])
	patient_id = IntegerField("Patient ID", validators=[DataRequired()])
	patient_name = StringField("Name", validators=[DataRequired(), Length(max=20)])
	patient_address = StringField("Address", validators=[DataRequired(), Length(max=100)])
	patient_age = IntegerField("Age", validators=[DataRequired()])
	patient_DOJ = DateField("Date of joining", default=dt.today(), validators=[DataRequired()])
	patient_DOD = DateField("Date of discharge", validators=[])
	patient_room_type = SelectField("Room Type", validators=[DataRequired()], choices=[('Single', 'Single'), ('Shared', 'Shared'), ('General', 'General')])
	patient_state = SelectField("State",validators=[DataRequired()],choices=[("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry")])
	patient_city = SelectField("City",validators=[DataRequired()],choices=[('Mumbai', 'Mumbai'), ('Delhi', 'Delhi'), ('Kolkata', 'Kolkata'), ('Chennai', 'Chennai'), ('Bengalūru', 'Bengalūru'), ('Hyderabad', 'Hyderabad'), ('Ahmadābād', 'Ahmadābād'), ('Hāora', 'Hāora'), ('Pune', 'Pune'), ('Sūrat', 'Sūrat'), ('Mardānpur', 'Mardānpur'), ('Rāmpura', 'Rāmpura'), ('Lucknow', 'Lucknow'), ('Nāra', 'Nāra'), ('Patna', 'Patna'), ('Indore', 'Indore'), ('Vadodara', 'Vadodara'), ('Bhopal', 'Bhopal'), ('Coimbatore', 'Coimbatore'), ('Ludhiāna', 'Ludhiāna'), ('Āgra', 'Āgra'), ('Kalyān', 'Kalyān'), ('Vishākhapatnam', 'Vishākhapatnam'), ('Kochi', 'Kochi'), ('Nāsik', 'Nāsik'), ('Meerut', 'Meerut'), ('Farīdābād', 'Farīdābād'), ('Vārānasi', 'Vārānasi'), ('Ghāziābād', 'Ghāziābād'), ('Āsansol', 'Āsansol'), ('Jamshedpur', 'Jamshedpur'), ('Madurai', 'Madurai'), ('Jabalpur', 'Jabalpur'), ('Rājkot', 'Rājkot'), ('Dhanbād', 'Dhanbād'), ('Amritsar', 'Amritsar'), ('Warangal', 'Warangal'), ('Allahābād', 'Allahābād'), ('Srīnagar', 'Srīnagar'), ('Aurangābād', 'Aurangābād'), ('Bhilai', 'Bhilai'), ('Solāpur', 'Solāpur'), ('Ranchi', 'Ranchi'), ('Jodhpur', 'Jodhpur'), ('Guwāhāti', 'Guwāhāti'), ('Chandigarh', 'Chandigarh'), ('Gwalior', 'Gwalior'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Tiruchchirāppalli', 'Tiruchchirāppalli'), ('Hubli', 'Hubli'), ('Mysore', 'Mysore'), ('Raipur', 'Raipur'), ('Salem', 'Salem'), ('Bhubaneshwar', 'Bhubaneshwar'), ('Kota', 'Kota'), ('Jhānsi', 'Jhānsi'), ('Bareilly', 'Bareilly'), ('Alīgarh', 'Alīgarh'), ('Bhiwandi', 'Bhiwandi'), ('Jammu', 'Jammu'), ('Morādābād', 'Morādābād'), ('Mangalore', 'Mangalore'), ('Kolhāpur', 'Kolhāpur'), ('Amrāvati', 'Amrāvati'), ('Dehra Dūn', 'Dehra Dūn'), ('Mālegaon Camp', 'Mālegaon Camp'), ('Nellore', 'Nellore'), ('Gopālpur', 'Gopālpur'), ('Shimoga', 'Shimoga'), ('Tiruppūr', 'Tiruppūr'), ('Raurkela', 'Raurkela'), ('Nānded', 'Nānded'), ('Belgaum', 'Belgaum'), ('Sāngli', 'Sāngli'), ('Chānda', 'Chānda'), ('Ajmer', 'Ajmer'), ('Cuttack', 'Cuttack'), ('Bīkaner', 'Bīkaner'), ('Bhāvnagar', 'Bhāvnagar'), ('Hisar', 'Hisar'), ('Bilāspur', 'Bilāspur'), ('Tirunelveli', 'Tirunelveli'), ('Guntūr', 'Guntūr'), ('Shiliguri', 'Shiliguri'), ('Ujjain', 'Ujjain'), ('Davangere', 'Davangere'), ('Akola', 'Akola'), ('Sahāranpur', 'Sahāranpur'), ('Gulbarga', 'Gulbarga'), ('Bhātpāra', 'Bhātpāra'), ('Dhūlia', 'Dhūlia'), ('Udaipur', 'Udaipur'), ('Bellary', 'Bellary'), ('Tuticorin', 'Tuticorin'), ('Kurnool', 'Kurnool'), ('Gaya', 'Gaya'), ('Sīkar', 'Sīkar'), ('Tumkūr', 'Tumkūr'), ('Kollam', 'Kollam'), ('Ahmadnagar', 'Ahmadnagar'), ('Bhīlwāra', 'Bhīlwāra'), ('Nizāmābād', 'Nizāmābād'), ('Parbhani', 'Parbhani'), ('Shillong', 'Shillong'), ('Lātūr', 'Lātūr'), ('Rājapālaiyam', 'Rājapālaiyam'), ('Bhāgalpur', 'Bhāgalpur'), ('Muzaffarnagar', 'Muzaffarnagar'), ('Muzaffarpur', 'Muzaffarpur'), ('Mathura', 'Mathura'), ('Patiāla', 'Patiāla'), ('Saugor', 'Saugor'), ('Brahmapur', 'Brahmapur'), ('Shāhbāzpur', 'Shāhbāzpur'), ('New Delhi', 'New Delhi'), ('Rohtak', 'Rohtak'), ('Samlaipādar', 'Samlaipādar'), ('Ratlām', 'Ratlām'), ('Fīrozābād', 'Fīrozābād'), ('Rājahmundry', 'Rājahmundry'), ('Barddhamān', 'Barddhamān'), ('Bīdar', 'Bīdar'), ('Bamanpurī', 'Bamanpurī'), ('Kākināda', 'Kākināda'), ('Pānīpat', 'Pānīpat'), ('Khammam', 'Khammam'), ('Bhuj', 'Bhuj'), ('Karīmnagar', 'Karīmnagar'), ('Tirupati', 'Tirupati'), ('Hospet', 'Hospet'), ('Chikka Mandya', 'Chikka Mandya'), ('Alwar', 'Alwar'), ('Aizawl', 'Aizawl'), ('Bijāpur', 'Bijāpur'), ('Imphal', 'Imphal'), ('Tharati Etawah', 'Tharati Etawah'), ('Rāichūr', 'Rāichūr'), ('Pathānkot', 'Pathānkot'), ('Chīrāla', 'Chīrāla'), ('Sonīpat', 'Sonīpat'), ('Mirzāpur', 'Mirzāpur'), ('Hāpur', 'Hāpur'), ('Porbandar', 'Porbandar'), ('Bharatpur', 'Bharatpur'), ('Puducherry', 'Puducherry'), ('Karnāl', 'Karnāl'), ('Nāgercoil', 'Nāgercoil'), ('Thanjāvūr', 'Thanjāvūr'), ('Pāli', 'Pāli'), ('Agartala', 'Agartala'), ('Ongole', 'Ongole'), ('Puri', 'Puri'), ('Dindigul', 'Dindigul'), ('Haldia', 'Haldia'), ('Bulandshahr', 'Bulandshahr'), ('Purnea', 'Purnea'), ('Proddatūr', 'Proddatūr'), ('Gurgaon', 'Gurgaon'), ('Khānāpur', 'Khānāpur'), ('Machilīpatnam', 'Machilīpatnam'), ('Bhiwāni', 'Bhiwāni'), ('Nandyāl', 'Nandyāl'), ('Bhusāval', 'Bhusāval'), ('Bharauri', 'Bharauri'), ('Tonk', 'Tonk'), ('Sirsa', 'Sirsa'), ('Vizianagaram', 'Vizianagaram'), ('Vellore', 'Vellore'), ('Alappuzha', 'Alappuzha'), ('Shimla', 'Shimla'), ('Hindupur', 'Hindupur'), ('Bāramūla', 'Bāramūla'), ('Bakshpur', 'Bakshpur'), ('Dibrugarh', 'Dibrugarh'), ('Saidāpur', 'Saidāpur'), ('Navsāri', 'Navsāri'), ('Budaun', 'Budaun'), ('Cuddalore', 'Cuddalore'), ('Harīpur', 'Harīpur'), ('Krishnāpuram', 'Krishnāpuram'), ('Fyzābād', 'Fyzābād'), ('Silchar', 'Silchar'), ('Ambāla', 'Ambāla'), ('Krishnanagar', 'Krishnanagar'), ('Kolār', 'Kolār'), ('Kumbakonam', 'Kumbakonam'), ('Tiruvannāmalai', 'Tiruvannāmalai'), ('Pīlibhīt', 'Pīlibhīt'), ('Abohar', 'Abohar'), ('Port Blair', 'Port Blair'), ('Alīpur Duār', 'Alīpur Duār'), ('Hatīsa', 'Hatīsa'), ('Vālpārai', 'Vālpārai'), ('Aurangābād', 'Aurangābād'), ('Kohima', 'Kohima'), ('Gangtok', 'Gangtok'), ('Karūr', 'Karūr'), ('Jorhāt', 'Jorhāt'), ('Panaji', 'Panaji'), ('Saidpur', 'Saidpur'), ('Tezpur', 'Tezpur'), ('Itanagar', 'Itanagar'), ('Daman', 'Daman'), ('Silvassa', 'Silvassa'), ('Diu', 'Diu'), ('Dispur', 'Dispur'), ('Kavaratti', 'Kavaratti'), ('Calicut', 'Calicut'), ('Kagaznāgār', 'Kagaznāgār'), ('Jaipur', 'Jaipur'), ('Ghandinagar', 'Ghandinagar'), ('Panchkula', 'Panchkula')])
	patient_status = SelectField("Status", validators=[DataRequired()], choices=[('Active', 'Active'), ('Inactive', 'Inactive')])
	submit = SubmitField("Submit Details")

	def validate_ssn(self, ssn):
		if ssn.data < 10000000:
			raise ValidationError("SSN should be atleast 8 digits!!!")

	def validate_patient_id(self, patient_id):
		if patient_id.data < 10000000:
			raise ValidationError("Patient ID should be atleast 8 digits!!!")

	@staticmethod
	def generate_patient_id():
		first_patient_id = Patient.query.first().patient_id
		total_patients = len(Patient.query.all())
		nextPatientID = first_patient_id + total_patients + 1
		return nextPatientID

class ConfirmationForm(FlaskForm):
	confirm = BooleanField("Yes", default=True)
	patient_id = IntegerField("Patient ID", validators=[DataRequired()])
	submit = SubmitField("Confirm")