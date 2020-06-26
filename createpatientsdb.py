from hms import db, bcrypt
from hms.models import Patient
import random as rd
from datetime import date as dt

names = ["Liam",
"Noah",
"William",
"James",
"Oliver",
"Benjamin",
"Elijah",
"Lucas",
"Mason",
"Logan",
"Alexander",
"Ethan",
"Jacob",
"Michael",
"Daniel",
"Henry",
"Jackson",
"Sebastian",
"Aiden",
"Matthew",
"Samuel",
"David",
"Joseph",
"Carter",
"Owen",
"Wyatt",
"John",
"Jack",
"Luke",
"Jayden",
"Dylan",
"Grayson",
"Levi",
"Isaac",
"Gabriel",
"Julian",
"Mateo",
"Anthony",
"Jaxon",
"Lincoln"]

addr = ["17 S Chester Rd, Swarthmore, PA, 19081",
"44064 Engle Way #APT 83, Lancaster, CA, 93536",
"Po Box 7570, Urbandale, IA, 50323",
"1502 Murray Ln, Chapel Hill, NC, 27517",
"415 Page Pl, Roswell, GA, 30076",
"229 Secretariat Ct, Ashland, VA, 23005",
"3209 S Michigan St, South Bend, IN, 46614",
"1711 Eagle Watch Dr, Orange Park, FL, 32003",
"9105 79th St S, Cottage Grove, MN, 55016",
"411 Fairway St, Pearisburg, VA, 24134",
]

state=[
"Andra Pradesh",
"Arunachal Pradesh",
"Assam",
"Bihar",
"Chhattisgarh",
"Goa",
"Gujarat",
"Haryana",
"Himachal Pradesh",
"Jammu and Kashmir",
"Jharkhand",
"Karnataka",
"Kerala",
"Madya Pradesh",
"Maharashtra",
"Manipur",
"Meghalaya",
"Mizoram",
"Nagaland",
"Orissa",
"Punjab",
"Rajasthan",
"Sikkim",
"Tamil Nadu",
"Telagana",
"Tripura",
"Uttaranchal",
"Uttar Pradesh",
"West Bengal",
]

city = [
"Hyderabad",
"Itangar",
"Dispur",
"Patna",
"Raipur",
"Panaji",
"Gandhinagar",
"Chandigarh",
"Shimla",
"Srinagar",
"Ranchi",
"Bangalore",
"Thiruvananthapuram",
"Bhopal",
"Mumbai",
"Imphal",
"Shillong",
"Aizawi",
"Kohima",
"Bhubaneshwar",
"Chandigarh",
"Jaipur",
"Gangtok",
"Chennai",
"Hyderabad",
"Agartala",
"Dehradun",
"Lucknow",
"Kolkata",
]

roomtypes = ["single", "shared", "general"]

status = ["active", "inactive"]

ssnNo = rd.randint(77777777,99999999)
patient_id = rd.randint(33333333, 99999999)
for i in range(25):
	randomstatecity = rd.randint(0,28)
	patient = Patient(ssn=ssnNo+1, patient_id=patient_id+1, patient_name=names[rd.randint(0,39)], patient_address=addr[rd.randint(0, 9)], patient_age=rd.randint(10,80), patient_DOJ=dt(rd.randint(2019,2020), rd.randint(1,12), rd.randint(1,30)), patient_DOD=dt(rd.randint(2019,2020), rd.randint(1,12), rd.randint(1,30)), patient_state=state[randomstatecity], patient_city=city[randomstatecity], patient_room_type=roomtypes[rd.randint(0, 2)], patient_status=status[rd.randint(0, 1)])
	print(patient)
	ssnNo+=1
	patient_id+=1
	db.session.add(patient)
	db.session.commit()

patients = Patient.query.all()
for patient in patients:
	print(patient)