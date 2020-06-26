from hms import db, bcrypt
from hms.models import User
import random as rd

'''
There will be 5 users with random access as teller and acc_exec
'''

idStart = 11111
role=["adm_desk", "pharm", "diag"]
for _ in range(9):
	username = "User"+str(idStart+11111)
	password = "User@"+str(idStart+11111)
	password = bcrypt.generate_password_hash(password).decode('utf-8')
	user = User(username=username, password=password, role=role[rd.randint(0, 2)])
	db.session.add(user)
	db.session.commit()
	idStart += 11111
	print("user added", user)

users = User.query.all()
for user in users:
	print(user)
print(len(users))

