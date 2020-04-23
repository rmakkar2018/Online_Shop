from OnlineShop import *

def dbCustomerReg(name,email,mobile,address,credit_card):
	print("")
	print("Registring Customer.........................")
	return 1

def customerRegistration():
	print("")
	name = str(input("Name : "))
	email = str(input("Email Id : "))
	mobile = str(input("Mobile No. : "))		
	address = str(input("Address : "))
	credit_card = str(input("Credit Card No. : "))
	if(dbCustomerReg(name,email,mobile,address,credit_card) == 1):
		print("Customer Registered SuccessFully")
	else:
		print("Customer Registration Failed")

def dbSupplierReg(name,email,mobile,address,gst):
	print("")
	print("Registring Supplier........................")
	return 1

def supplierRegistration():
	print("")
	name = str(input("Name : "))
	email = str(input("Email Id : "))
	mobile = str(input("Mobile No. : "))		
	address = str(input("Address : "))
	gst = str(input("GST No. : "))
	if(dbSupplierReg(name,email,mobile,address,gst) == 1):
		print("Supplier Registered SuccessFully")
	else:
		print("Supplier Registration Failed")



def signUpOptions():
	print("")
	print("------------Welcome to Registration Portal--------------")
	while(True):
		print("")
		print("Choose Role")
		print("1. Customer")
		print("2. Supplier")
		print("3. Exit")
		option = int(input("Enter your choice ==> "))
		if(option == 1):
			customerRegistration()
		elif(option == 2):
			supplierRegistration()
		elif(option == 3):
			print("Exiting Registration Portal")
			break
		else:
			print("Enter a valid option")