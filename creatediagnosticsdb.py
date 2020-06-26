from hms import db, bcrypt
from hms.models import Patient, Diagnostics
import random as rd

diagnostics_id = rd.randint(55555555, 99999999)

patients = Patient.query.all()

diag_names = [
'amniocentesis',
'blood analysis',
'blood count',
'blood typing',
'bone marrow aspiration',
'cephalin-cholesterol flocculation',
'enzyme analysis',
'epinephrine tolerance test',
'glucose tolerance test',
'hematocrit',
'immunologic blood test',
'inulin clearance',
'thymol turbidity',
'serological test',
'gastric fluid analysis',
'kidney function test',
'liver function test',
'lumbar puncture',
'malabsorption test',
'Pap smear',
'phenolsulfonphthalein test',
'pregnancy test',
'prenatal testing',
'protein-bound iodine test',
'syphilis test',
'thoracentesis',
'thyroid function test',
'toxicology test',
'urinalysis/uroscopy'
]

for patient in patients:
	diagnostics1 = Diagnostics(diagnostics_id=diagnostics_id, diagnostics_name=diag_names[rd.randint(0,28)], diagnostics_amount=float(rd.randint(5000,20000)), patient_id=patient.patient_id)
	print(diagnostics1)
	db.session.add(diagnostics1)
	db.session.commit()
	diagnostics_id += 1
	diagnostics2 = Diagnostics(diagnostics_id=diagnostics_id, diagnostics_name=diag_names[rd.randint(0,28)], diagnostics_amount=float(rd.randint(5000,20000)), patient_id=patient.patient_id)
	print(diagnostics2)
	db.session.add(diagnostics2)
	db.session.commit()
	diagnostics_id += 1
	diagnostics3 = Diagnostics(diagnostics_id=diagnostics_id, diagnostics_name=diag_names[rd.randint(0,28)], diagnostics_amount=float(rd.randint(5000,20000)), patient_id=patient.patient_id)
	print(diagnostics3)
	db.session.add(diagnostics3)
	db.session.commit()
	diagnostics_id += 1

diagnostics = Diagnostics.query.all()
for diag in diagnostics:
	print(diag)

print(len(diagnostics))