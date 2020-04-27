from global_db import *

def check_id_pass(id,password):
	query="Select count(id) from ID_Pass where id="+str(id)+" and password="+password+";"
	cursor=db.cursor()
	cursor.execute(query)
	l=fetchdetails(cursor)[0][0]
	if(l==0):
		return 0
	else:
		return 1

def customerDbQuery(uid,password):
	if(len(uid)==0):
		print("Enter a valid Customer Id")
		return 0
	if(len(password) == 0):
		print("Enter a valid password")
		return 0
	return check_id_pass(uid,password)

def loginCustomerWithCreds(uid,password):
	from CustomerMainScreen import enterCustomerMainScreen
	if(customerDbQuery(uid,password) == 1):
		enterCustomerMainScreen(uid);
	else:
		print("")
		print("Login Failed")

def customerLogin():
	while(True):
		print("")
		print("---------------------Customer Login---------------------")
		uid = str(input("Customer Id: "))
		password = str(input("Password: "))
		print("")
		print("1. Login")
		print("2. Exit")
		option = input("Enter your choice ==> ")
		if(option == '1'):
			loginCustomerWithCreds(uid,password);
		elif(option == '2'):
			print("")
			print("Exiting from Login Portal")
			clear()
			print("---------------------Login Portal---------------------")
			break
		else:
			print("Enter a valid option")

def supplierDbQuery(uid,password):
	if(len(uid) == 0):
		print("Enter a valid Supplier Id")
		return 0
	if(len(password) == 0):
		print("Enter a valid password")
		return 0
	return check_id_pass(uid,password)

def loginSupplierWithCreds(uid,password):
	from SupplierMainScreen import enterSupplierMainScreen
	if(supplierDbQuery(uid,password) == 1):
		enterSupplierMainScreen(uid);
	else:
		print("")
		print("Login Failed")

def supplierLogin():
	while(True):
		print("")
		print("---------------------Supplier Login---------------------")
		uid = str(input("Supplier Id: "))
		password = str(input("Password: "))
		print("")
		print("1. Login")
		print("2. Exit")
		option = input("Enter your choice ==> ")
		if(option == '1'):
			loginSupplierWithCreds(uid,password);
		elif(option == '2'):
			print("Exiting from Login Portal")
			clear()
			print("---------------------Login Portal---------------------")
			break
		else:
			print("Enter a valid option")

def employeeDbQuery(uid,password):
	if(len(uid) == 0):
		print("Enter a valid Emplyee Id")
		return 0
	if(len(password) == 0):
		print("Enter a valid password")
		return 0
	return check_id_pass(uid,password)

def loginEmployeeWithCreds(uid,password):
	from EmployeeMainScreen import enterEmployeeMainScreen
	if(employeeDbQuery(uid,password) == 1):
		enterEmployeeMainScreen(uid);
	else:
		print("")
		print("Login Failed")

def employeeLogin():
	while(True):
		print("")
		print("---------------------Employee Login---------------------")
		uid = str(input("Employee Id: "))
		password = str(input("Password: "))
		print("")
		print("1. Login")
		print("2. Exit")
		option = input("Enter your choice ==> ")
		if(option == '1'):
			loginEmployeeWithCreds(uid,password);
		elif(option == '2'):
			print("Exiting from Login Portal")
			clear()
			print("---------------------Login Portal---------------------")
			break
		else:
			print("Enter a valid option")

def managerDbQuery(uid,password):
	if(len(uid) == 0):
		print("Enter a valid Manager Id")
		return 0
	if(len(password) == 0):
		print("Enter a valid password")
		return 0
	return check_id_pass(uid,password)

def loginManagerWithCreds(uid,password):
	from ManagerMainScreen import enterManagerMainScreen
	if(employeeDbQuery(uid,password) == 1):
		enterManagerMainScreen(uid);
	else:
		print("")
		print("Login Failed")

def managerLogin():
	while(True):
		print("")
		print("---------------------Manager Login---------------------")
		uid = str(input("Manager Id: "))
		password = str(input("Password: "))
		print("")
		print("1. Login")
		print("2. Exit")
		option = input("Enter your choice ==> ")
		if(option == '1'):
			loginManagerWithCreds(uid,password);
		elif(option == '2'):
			print("Exiting from Login Portal")
			clear()
			print("---------------------Login Portal---------------------")
			break
		else:
			print("Enter a valid option")

def ownerDbQuery(uid,password):
	if(len(uid) == 0):
		print("Enter a valid Owner Id")
		return 0
	if(len(password) == 0):
		print("Enter a valid password")
		return 0
	return check_id_pass(uid,password)

def loginOwnerWithCreds(uid,password):
	from OwnerMainScreen import enterOwnerMainScreen 
	if(ownerDbQuery(uid,password) == 1):
		enterOwnerMainScreen(uid);
	else:
		print("")
		print("Login Failed")

def ownerLogin():
	while(True):
		print("")
		print("---------------------Owner Login---------------------")
		uid = str(input("Owner Id: "))
		password = str(input("Password: "))
		print("")
		print("1. Login")
		print("2. Exit")
		option = input("Enter your choice ==> ")
		if(option == '1'):
			loginOwnerWithCreds(uid,password);
		elif(option == '2'):
			print("Exiting from Login Portal")
			clear()
			print("---------------------Login Portal---------------------")
			break
		else:
			print("Enter a valid option")

def loginOptions():
	clear()
	print("---------------------Login Portal---------------------")
	while(True):
		print("")
		print("Choose Role")
		print("1. Customer")
		print("2. Supplier")
		print("3. Employee")
		print("4. Manager")
		print("5. Owner")
		print("6. Exit")
		option = input("Enter your choice ==> ")
		if(option == '1'):
			clear()
			customerLogin()
		elif(option == '2'):
			clear()
			supplierLogin()
		elif(option == '3'):
			clear()
			employeeLogin()
		elif(option == '4'):
			clear()
			managerLogin()
		elif(option == '5'):
			clear()
			ownerLogin()
		elif(option == '6'):
			clear()
			break;
		else:
			print("Choose a valid option")