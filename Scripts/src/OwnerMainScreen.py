# manager register
# view everthing
# manager, customer, employee delete all
from os import system,name
def clear(): 
	if name == 'nt': 
		_ = system('cls') 
	else: 
		_ = system('clear') 
def Owner_mainScreen():
	while True:
		print(" ----------------------------------- Welcome ----------------------------------")
		print("")
		print("1. Register")
		print("2. View")
		print("3. Remove")
		print("4. Logout")
		option = input(" Enter your choice: ")
		if option == '1':
			Register();
		elif option == '2':
			View()
		elif option == '3': 
			Remove()
		elif option == '4':
			clear()
			break
		else:
			print(" Enter a valid choice: ")

def Register():
	clear()
	while True:
		print(" Welcome :)")
		print("")
		print("1. Register a Manager ")
		print("2. Register an employee ")
		print("3. Go back")
		option = input(" Enter the choice: ")
		if option == '1':
			Register_manager()
		elif option == '2':
			Register_employee()
		elif option == '3':
			clear()
			break
		else:
			print(" Enter a valid choice: ")


def Register_manager():
	print(" --------------------- Welcome to Manager registartion ---------------------------- ")
	print("")
	print(" Enter the details")
	# get the details query

	print(" The Manager has been registered ")
	print(" Welcome to the Team")

def Register_employee():
	print("------------------- Welcome to Employee registration ------------------------------")
	print(" Enter the details of the Employee")
	#get the details to be entered into  the table

	print(" Employee has been registered")
	print(" Welcome to the team")

def View():
	clear()
	while True:
		print("-------------------------- Profile Section ----------------------------------------")
		print("")
		print("1. View Profile of Manager")
		print("2. View Profile of Employee")
		print("3. View profile of Supplier")
		print("4. Go back")
		option = input(" Enter the choice: ")
		if option == '1':
			View_manager()
		elif option == '2':
			View_employee()
		elif option == '3':
			View_supplier()
		elif option == '4':
			clear()
			break
		else:
			print(" Enter a valid choice: ")

def View_manager():
	clear()
	while True:
		print("----------------------------- Manager Profile ------------------------------------")
		print("1. Know manager ID")
		print("2. Search Manager")
		print("3. Go back")
		option = input("Enter the choice: ")
		if option == '1':
			ManagerID = input(" Enter Manager ID: ")
			View_managerID(ManagerID)
			# return
		elif option == '2':
			ManagerID = Search_manager()
			View_managerID(ManagerID)
			# return
		elif option == '3':
			clear()
			break
		else :
			print("Enter a valid choice: ")

def View_managerID(ManagerID):
	#print the details of manager
	print(" Manager Details: ")

def Search_manager():
	# clear()
	while(True):
		print("------------------------ Search Manager ----------------------------------")
		print("1. Search by name: ")
		print("2. Search by date of joining")
		print("3. Go back")
		option = input(" Enter your choice: ")
		if option == '1':
			name = input("Enter the name of the Manager: ")
			#print all the manager with those name and their ID
			ManagerID = input(" Enter Manager ID: ")
			return ManagerID
		elif option == '2':
			date = input(" Enter the date of joining ")
			#print all the manager with those date and their ID
			ManagerID = input(" Enter Manager ID: ")
			return ManagerID
		elif option == '3':
			clear()
			break
		else:
			print(" Enter a valid choice: ")
	

def View_employee():
	clear()
	while True:
		print("----------------------------- Employee Profile ------------------------------------")
		print("1. Know employee ID")
		print("2. Search employee")
		print("3. Go back")
		option = input("Enter the choice: ")
		if option == '1':
			EmployeeID = input(" Enter Employee ID: ")
			View_employeeID(EmployeeID)
			# return
		elif option == '2':
			EmployeeID = Search_employee()
			View_employeeID(EmployeeID)
			# return
		elif option == '3':
			clear()
			break
		else:
			print(" Enter a valid choice: ")

def View_employeeID(EmployeeID):
	#print the details of manager
	print(" Empolyee Details: ")

def Search_employee():
	# clear()
	while(True):
		print("------------------------ Search Employee ----------------------------------")
		print("1. Search by name: ")
		print("2. Search by date of joining")
		print("3. Go back")
		option = input(" Enter your choice: ")
		if option == '1':
			name = input("Enter the name of the Employee: ")
			#print all the manager with those name and their ID
			EmployeeID = input(" Enter Employee ID: ")
			return EmployeeID
		elif option == '2':
			date = input(" Enter the date of joining ")
			#print all the manager with those date and their ID
			EmployeeID = input(" Enter Employee ID: ")
			return EmployeeID
		elif option == '3':
			clear()
			break
		else:
			print(" Enter a valid choice: ")


def View_supplier():
	clear()
	while True:
		print("----------------------------- Supplier Profile ------------------------------------")
		print("1. Know Supplier ID")
		print("2. Search Supplier")
		print("3. Go back")
		option = input("Enter the choice: ")
		if option == '1':
			SupplierID = input(" Enter Supplier ID: ")
			View_supplierID(SupplierID)
		elif option == '2':
			SupplierID = Search_supplier()
			View_supplierID(SupplierID)
		elif option == '3':
			clear()
			break

def View_supplierID(SupplierID):
	#print the details of manager
	print(" Supplier Details: ")

def Search_supplier():
	# clear()
	while(True):
		print("------------------------ Search Supplier ----------------------------------")
		print("1. Search by name: ")
		print("2. Search by date of joining")
		print("3. Go back")
		option = input(" Enter your choice: ")
		if option == '1':
			name = input("Enter the name of the Supplier: ")
			#print all the manager with those name and their ID
			SupplierID = input(" Enter Supplier ID: ")
			return SupplierID
		elif option == '2':
			date = input(" Enter the date of joining ")
			#print all the manager with those date and their ID
			SupplierID = input(" Enter Supplier ID: ")
			return SupplierID
		elif option == '3':
			clear()
			break
		else:
			print(" Enter a valid choice: ")


def Remove():
	clear()
	while(True):
		print("--------------------------- Someone is going to be fired today ------------------------")
		print("")
		print("1. Remove a manager")
		print("2. Remove an employee")
		print("3. Remove a supplier")
		print("4. Remove a customer")
		print("5. Go back")
		option = input(" Enter whom you want to remove: ")
		if option == '1':
			Remove_manager()
		elif option == '2':
			Remove_employee()
		elif option == '3':
			Remove_supplier()
		elif option == '4':
			Remove_customer()
		elif option == '5':
			print(" Rest are safe ;) ")
			clear()
			break
		else:
			print(" Enter a valid choice")

def Remove_manager():
	while True:
		print("1. Know manager ID")
		print("2. Search Manager")
		print("3. Go back")
		option = input("Enter the choice: ")
		if option == '1':
			ManagerID = input(" Enter Manager ID: ")
			Remove_managerID(ManagerID)		
		elif option == '2':
			ManagerID = Search_manager()
			Remove_managerID(ManagerID)		
		elif option == '3':
			clear()
			break
		else:
			print(" Enter a valid choice: ")

def Remove_managerID(ManagerID):
	#remove that manager from manager table
	print("------------------- Manager removed successfully ---------------------------")



def Remove_employee():
	while True:
		print("1. Know employee ID")
		print("2. Search employee")
		print("3. Go back")
		option = input("Enter the choice: ")
		if option == '1':
			EmployeeID = input(" Enter the Employee ID to be reomved: ")
			Remove_employeeID(EmployeeID)		
		elif option == '2':
			EmployeeID = Search_employee()
			Remove_employeeID(EmployeeID)		
		elif option == '3':
			clear()
			break
		else:
			print(" Enter a vaild choice: ")

def Remove_employeeID(EmployeeID):
	# remove the employee from employee table
	print("------------------- Employee removed successfully ----------------------------")

def Remove_supplier():
	# SupplierID = input("Enter the supplier ID to be removed: ")
	while True:
		print(" You will also loose the data of items supplied by the supplier")
		print(" Do you want to continue[Y/N]: ")
		option = input()
		if option == 'Y':
			#remove the employee
			while True:
				print("1. Know supplier ID")
				print("2. Search supplier")
				print("3. Go back")
				option = input("Enter the choice: ")
				if option == '1':
					SupplierID = input(" Enter the Supplier ID to be reomved: ")
					Remove_supplierID(SupplierID)		
				elif option == '2':
					SupplierID = Search_supplier()
					Remove_supplierID(SupplierID)		
				elif option == '3':
					clear()
					break
				else:
					print(" Enter a vaild choice: ")
			# print(" Supplier removed successfully")
		elif option == 'N':
			break
def Remove_supplierID(SupplierID):
	#remove the supplier
	print("------------------------- Supplier removed successfully --------------------------")

def Remove_customer():
	# customerID = input(" Enter the customer ID to be removed")
	while True:
		print(" You will loose a valuable customer")
		print(" Do you want to continue[Y/N]: ")
		option = input()
		if option == 'Y':
			#remove the employee
			while True:
				print("1. Know customer ID")
				print("2. Search customer")
				print("3. Go back")
				option = input("Enter the choice: ")
				if option == '1':
					CustomerID = input(" Enter the Customer ID to be reomved: ")
					Remove_customerID(CustomerID)		
				elif option == '2':
					CustomerID = Search_customer()
					Remove_customerID(CustomerID)		
				elif option == '3':
					clear()
					break
				else:
					print(" Enter a vaild choice: ")
		elif option == 'N':
			break

def Remove_customerID(CustomerID):
	#remove the customer
	print("-----------------------Customer removed successfully--------------------")

def Search_customer():
	clear()
	while(True):
		print("------------------------ Search Customer ----------------------------------")
		print("1. Search by name: ")
		print("2. Go back")
		option = input(" Enter your choice: ")
		if option == '1':
			name = input("Enter the name of the Customer: ")
			#print all the manager with those name and their ID
			CustomerID = input(" Enter Customer ID: ")
			return CustomerID
		elif option == '2':
			clear()
			break
		else:
			print(" Enter a valid choice: ")
	


