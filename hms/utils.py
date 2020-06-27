from datetime import date

def calculate_days(patient_DOJ, patient_DOD):
	delta = patient_DOD - patient_DOJ
	days = delta.days
	return days

def calculate_room_fees(room_type, days):
	if room_type.lower() == "general":
		per_day_fees = 2000
	elif room_type.lower() == "shared":
		per_day_fees = 4000
	elif room_type.lower() == "single":
		per_day_fees = 8000
	return (per_day_fees*days)

