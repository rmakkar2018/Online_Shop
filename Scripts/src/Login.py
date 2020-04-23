from CustomerMainScreen import *
from SupplierMainScreen import *
from EmployeeMainScreen import *

def customerDbQuery(uid,password):
	return 1;

def loginCustomerWithCreds(uid,password):
	if(customerDbQuery(uid,password) == 1):
		enterCustomerMainScreen(uid);
	else:
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
		option = int(input("Enter your choice ==> "))
		if(option == 1):
			loginCustomerWithCreds(uid,password);
		elif(option == 2):
			print("Exiting from Login Portal")
			break
		else:
			print("Enter a valid option")

def supplierDbQuery(uid,password):
	return 1;

def loginSupplierWithCreds(uid,password):
	if(supplierDbQuery(uid,password) == 1):
		enterSupplierMainScreen(uid);
	else:
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
		option = int(input("Enter your choice ==> "))
		if(option == 1):
			loginSupplierWithCreds(uid,password);
		elif(option == 2):
			print("Exiting from Login Portal")
			break
		else:
			print("Enter a valid option")

def employeeDbQuery(uid,password):
	return 1;

def loginEmployeeWithCreds(uid,password):
	if(employeeDbQuery(uid,password) == 1):
		enterEmployeeMainScreen(uid);
	else:
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
		option = int(input("Enter your choice ==> "))
		if(option == 1):
			loginEmployeeWithCreds(uid,password);
		elif(option == 2):
			print("Exiting from Login Portal")
			break
		else:
			print("Enter a valid option")

def loginOptions():
	while(True):
		print("")
		print("Choose Role")
		print("1. Customer")
		print("2. Supplier")
		print("3. Employee")
		print("4. Exit")
		option = int(input("Enter your choice ==> "))
		if(option == 1):
			customerLogin()
		elif(option == 2):
			supplierLogin()
		elif(option == 3):
			employeeLogin()
		elif(option == 4):
			break;
		else:
			print("Choose a valid option")