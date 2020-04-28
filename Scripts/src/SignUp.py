from global_db import *

def dbCustomerReg(name,email,mobile,address,credit_card,password,confPassword):
	if(len(name) == 0):
		print("Enter a valid name")
		return 0
	if(len(email) == 0):
		print("Enter a valid email id")
		return 0
	if(len(mobile) == 0):
		print("Enter a valid mobile no.")
		return 0
	if(len(address) == 0):
		print("Enter a valid address")
		return 0
	if(len(credit_card) == 0):
		print("Enter a valid a credit_card number")
		return 0
	if(len(password)==0):
		print("Enter a valid passowrd")
		return 0
	if(password!=confPassword):
		print("Passwords do not match.")
		return 0
	if(isInt(mobile) == 0):
		print("Enter a valid mobile number")
		return 0
	if(check(email) == 0):
		print("Enter a valid email id")
		return 0
	if(isInt(credit_card) == 0):
		print("Enter a valid credit card number")
		return 0
	id=fetch_id()+1
	cart_id=fetch_id()+2
	query="insert into Customer value (%s,%s,%s,%s,%s,%s,%s)"
	value=(id,name,int(mobile),address,email,int(credit_card),cart_id)
	cursor=db.cursor()
	print("")
	print("Registring Customer.........................")
	try:
		cursor.execute(query,value)
		reg_ID_Pass(id,password)
		update_id(id-1,2)
		print("--------------------------------------------------")
		print("ID Assigned- "+ str(id))
	except:
		return 0
	return 1

def customerRegistration():
	print("")
	name = str(input("Name : "))
	email = str(input("Email Id : "))
	mobile = str(input("Mobile No. : "))		
	address = str(input("Address : "))
	credit_card = str(input("Credit Card No. : "))
	password = str(input("Password : "))
	confPassWord = str(input("Confirm Password : "))
	if(dbCustomerReg(name,email,mobile,address,credit_card,password,confPassWord) == 1):
		print("")
		print("Customer Registered SuccessFully")
	else:
		print("")
		print("Customer Registration Failed")

def dbSupplierReg(name,email,mobile,address,gst,password,confPassword):
	if(len(name) == 0):
		print("Enter a valid name")
		return 0
	if(len(email) == 0):
		print("Enter a valid email id")
		return 0
	if(len(mobile) == 0):
		print("Enter a valid mobile no.")
		return 0
	if(len(address) == 0):
		print("Enter a valid address")
		return 0
	if(len(gst) == 0):
		print("Enter a valid a GST number")
		return 0
	if(len(password) == 0):
		print("Enter a valid passowrd")
		return 0
	if(password != confPassword):
		print("Passwords do not match.")
		return 0
	if(isInt(mobile) == 0):
		print("Enter a valid mobile number")
		return 0
	if(check(email) == 0):
		print("Enter a valid email id")
		return 0
	id=fetch_id()+1
	query="insert into Supplier value (%s,%s,%s,%s,%s,%s)"
	value=(id,name,int(mobile),email,address,gst)
	cursor=db.cursor()
	print("")
	print("Registring Supplier.........................")
	try:
		cursor.execute(query,value)
		reg_ID_Pass(id,password)
		update_id(id-1,1)
		print("ID Assigned- "+str(id))
	except:
		return 0
	return 1

def supplierRegistration():
	print("")
	name = str(input("Name : "))
	email = str(input("Email Id : "))
	mobile = str(input("Mobile No. : "))		
	address = str(input("Address : "))
	gst = str(input("GST No. : "))
	password = str(input("Password : "))
	confPassword = str(input("Confirm Password : "))
	if(dbSupplierReg(name,email,mobile,address,gst,password,confPassword) == 1):
		print("")
		print("Supplier Registered SuccessFully")
	else:
		print("")
		print("Supplier Registration Failed")

def signUpOptions():
	clear()
	print("")
	print("------------Welcome to Registration Portal--------------")
	while(True):
		print("")
		print("Choose Role")
		print("1. Customer")
		print("2. Supplier")
		print("3. Exit")
		option = input("Enter your choice ==> ")
		if(option == '1'):
			customerRegistration()
		elif(option == '2'):
			supplierRegistration()
		elif(option == '3'):
			print("Exiting Registration Portal")
			clear()
			break
		else:
			print("Enter a valid option")
