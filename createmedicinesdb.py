from hms import db, bcrypt
from hms.models import Patient, Medicine
import random as rd


medicine_names = [
'alendronate tablet	Fosamax',
'acyclovir capsule	Zovirax'
'acyclovir tablet	Zovirax',
'albuterol inhalation solution',
'Albuterol Inhalation Solution',
'albuterol sulfate	ProAir RespiClick Powder Inhaler',
'alclometasone dipropionate cream	Aclovate',
'alfuzosin hcl	Uroxatral',
'alitretinoin	Panretin gel',
'allopurinol tablet	Zyloprim',
'alprazolam	Xanax',
'altretamine	Hexalen capsules',
'amiodarone tablet	Cordarone',
'amitriptyline tablet	Elavil',
'amlodipine and valsartan	Exforge',
'amlodipine besylate	Norvasc',
'amlodipine, valsartan, hydrochlorothiazide	Exforge HCT',
'Amlodipine/Benazepril capsule	Lotrel',
'amoxapine tablet	Amoxapine tablet',
'anastrazole	Arimidex',
'antihypertensive combinations	Hyzaar',
'artificial tears	Artificial Tears',
'aspirin EC tablet (OTC)	Aspirin EC Tablet (OTC)',
'atenolol tablet	Tenormin',
'atenolol/chlorthalidone tablet	Tenoretic',
'atorvastatin calcium	Lipitor',
'augmented betamethasone dipropionate	Diprolene Cream',
'azathioprine	Imuran',
'azelastine	Astepro',
'Azelastine nasal spray	Astelin',
'baclofen tablet	Lioresal',
'Belladonna Alkaloids with Phenobarbital	Donnatal Tablet',
'benazepril HCTZ tablet	Lotensin HCT',
'benazepril tablet	Lotensin',
'benzonatate'
]



medicine_id = rd.randint(10000000, 11111111)

patients = Patient.query.all()
for patient in patients:
	medicine1 = Medicine(medicine_id=medicine_id, medicine_name=medicine_names[rd.randint(0,34)], medicine_quantity=rd.randint(15,25), medicine_rate=float(rd.randint(100,500)), medicine_amount=float(rd.randint(1000,5000)), patient_id=patient.patient_id)
	medicine_id += 1
	print(medicine1)
	db.session.add(medicine1)
	db.session.commit()
	medicine2 = Medicine(medicine_id=medicine_id, medicine_name=medicine_names[rd.randint(0,34)], medicine_quantity=rd.randint(15,25), medicine_rate=float(rd.randint(100,500)), medicine_amount=float(rd.randint(1000,5000)), patient_id=patient.patient_id)
	medicine_id += 1
	print(medicine2)
	db.session.add(medicine2)
	db.session.commit()
	medicine3 = Medicine(medicine_id=medicine_id, medicine_name=medicine_names[rd.randint(0,34)], medicine_quantity=rd.randint(15,25), medicine_rate=float(rd.randint(100,500)), medicine_amount=float(rd.randint(1000,5000)), patient_id=patient.patient_id)
	medicine_id += 1
	print(medicine3)
	db.session.add(medicine3)
	db.session.commit()
	medicine4 = Medicine(medicine_id=medicine_id, medicine_name=medicine_names[rd.randint(0,34)], medicine_quantity=rd.randint(15,25), medicine_rate=float(rd.randint(100,500)), medicine_amount=float(rd.randint(1000,5000)), patient_id=patient.patient_id)
	medicine_id += 1
	print(medicine4)
	db.session.add(medicine4)
	db.session.commit()
	medicine5 = Medicine(medicine_id=medicine_id, medicine_name=medicine_names[rd.randint(0,34)], medicine_quantity=rd.randint(15,25), medicine_rate=float(rd.randint(100,500)), medicine_amount=float(rd.randint(1000,5000)), patient_id=patient.patient_id)
	medicine_id += 1
	print(medicine5)
	db.session.add(medicine5)
	db.session.commit()
	

medicines = Medicine.query.all()
for medicine in medicines:
	print(medicine)

print(len(medicines))