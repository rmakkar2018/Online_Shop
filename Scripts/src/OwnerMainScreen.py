from global_db import *

def Owner_mainScreen():
	while True:
		print(" ----------------------------------- Welcome ----------------------------------")
		print("")
		print("1. Add a new Manager")
		print("2. View People")
		print("3. Show Stats")
		print("4. Logout")
		option = input(" Enter your choice: ")
		if option == '1':
			Register_manager();
		elif option == '2':
			View()
		elif option == '3': 
			show_stats()
		elif option == '4':
			clear()
			break
		else:
			print(" Enter a valid choice: ")

def Register_manager():
	print(" --------------------- Welcome to Manager registartion ---------------------------- ")
	print("")
	print("Enter the details")
	
	id=fetch_id()+1
	name=input("Enter Name: ")
	try:
		salary=float(input("Enter Salary: "))
		if(salary<=0):
			print("Please enter a valid value.")
			print("Registration failed.")
			return
	except:
		print("Please enter a valid value.")
		print("Registration failed.")
		return
	department=input("Enter department: ")
	email=input("Enter Email-ID: ")
	address=input("Enter Address: ")
	try:
		mobile=float(input("Enter Salary: "))
		if(mobile<=0):
			print("Please enter a valid value.")
			print("Registration failed.")
			return
	except:
		print("Please enter a valid value.")
		print("Registration failed.")
		return
	hire_date=date.today()
	try:
		query="insert into Manager value (%s,%s,%s,%s,%s,%s,%s,%s);"
		value=(id,name,salary,department,email,address,hire_date,mobile)
		cursor=db.cursor()
		cursor.execute(query,value)
		db.commit()
	except:
		print("Registration Failed. Please Try Again.")
		return
	print("The Manager has been registered.")
	print("Manager ID- "+str(id))
	print("Welcome to the Team")
	print()

def View():
	clear()
	while True:
		print("-------------------------- Profile Section ----------------------------------------")
		print("")
		print("1. View Profile of Manager")
		print("2. View Profile of Employee")
		print("3. View profile of Supplier")
		print("4. View profile of Customer")
		print("5. Go back")
		option = input(" Enter the choice: ")
		if option == '1':
			View_manager()
		elif option == '2':
			View_employee()
		elif option == '3':
			View_supplier()
		elif option == '4':
			View_customer()
		elif option == '5':
			clear()
			break
		else:
			print(" Enter a valid choice: ")

def View_manager():
	clear()
	while True:
		print("----------------------------- Manager Profile ------------------------------------")
		print("1. Search by Manager ID")
		print("2. Search by Manager Name")
		print("3. Go back")
		option = input("Enter the choice: ")
		if option == '1':
			ManagerID = input("Enter Manager ID: ")
			try:
				ManagerID=int(ManagerID)
			except:
				print("Enter a valid ID. Try Again.")
				continue
			query="select * from Manager where Manager_ID="+str(ManagerID)+";"
			cursor=db.cursor()
			cursor.execute(query)
			data=fetchdetails(cursor)
			if(len(data)==0):
				print("No Manager with this ID.")
			else:
				for i in data:
					print()
					print("Manager ID- "+str(i[0]))
					print("Name- "+str(i[1]))
					print("Department- "+str(i[3]))
					print("Mobile- "+str(i[7]))
					print("Email- "+str(i[4]))
					print("Address- "+str(i[5]))
					print("Salary- "+str(i[2]))
					print("Hire Date- "+str(i[6]))
				print()
		elif option == '2':
			ManagerName = input("Enter Manager Name: ")
			query="select * from Manager where Name like '%"+ManagerName+"%';"
			cursor=db.cursor()
			cursor.execute(query)
			data=fetchdetails(cursor)
			if(len(data)==0):
				print("No Manager with this Name.")
			else:
				for i in data:
					print()
					print("Manager ID- "+str(i[0]))
					print("Name- "+str(i[1]))
					print("Department- "+str(i[3]))
					print("Mobile- "+str(i[7]))
					print("Email- "+str(i[4]))
					print("Address- "+str(i[5]))
					print("Salary- "+str(i[2]))
					print("Hire Date- "+str(i[6]))
				print()
		elif option == '3':
			clear()
			break
		else :
			print("Enter a valid choice. Try Again")
	
def View_employee():
	clear()
	while True:
		print("----------------------------- Employee Profile ------------------------------------")
		print("1. Search by Employee ID")
		print("2. Search by Employee Name")
		print("3. Go back")
		option = input("Enter the choice: ")
		if option == '1':
			EmployeeID = input("Enter Employee ID: ")
			try:
				EmployeeID=int(EmployeeID)
			except:
				print("Enter a valid ID. Try Again.")
				continue
			query="select * from Employee where Employee_ID="+str(EmployeeID)+";"
			cursor=db.cursor()
			cursor.execute(query)
			data=fetchdetails(cursor)
			if(len(data)==0):
				print("No Employee with this ID.")
			else:
				for i in data:
					print()
					print("Employee ID- "+str(i[0]))
					print("Name- "+str(i[1]))
					print("Mobile- "+str(i[2]))
					print("Email- "+str(i[3]))
					print("Address- "+str(i[5]))
					print("Salary- "+str(i[4]))
					print("Hire Date- "+str(i[6]))
				print()
		elif option == '2':
			EmployeeName = input("Enter Employee Name: ")
			query="select * from Employee where Name like '%"+EmployeeName+"%';"
			cursor=db.cursor()
			cursor.execute(query)
			data=fetchdetails(cursor)
			if(len(data)==0):
				print("No Employee with this Name.")
			else:
				for i in data:
					print()
					print("Employee ID- "+str(i[0]))
					print("Name- "+str(i[1]))
					print("Mobile- "+str(i[2]))
					print("Email- "+str(i[3]))
					print("Address- "+str(i[5]))
					print("Salary- "+str(i[4]))
					print("Hire Date- "+str(i[6]))
				print()
		elif option == '3':
			clear()
			break
		else :
			print("Enter a valid choice. Try Again")

def View_supplier():
	clear()
	while True:
		print("----------------------------- Supplier Profile ------------------------------------")
		print("1. Search by Supplier ID")
		print("2. Search by Supplier Name")
		print("3. Go back")
		option = input("Enter the choice: ")
		if option == '1':
			SupplierID = input("Enter Supplier ID: ")
			try:
				SupplierID=int(SupplierID)
			except:
				print("Enter a valid ID. Try Again.")
				continue
			query="select * from Supplier where Supplier_ID="+str(SupplierID)+";"
			cursor=db.cursor()
			cursor.execute(query)
			data=fetchdetails(cursor)
			if(len(data)==0):
				print("No Supplier with this ID.")
			else:
				for i in data:
					print()
					print("Supplier ID: "+str(i[0]))
					print("Name: "+str(i[1]))
					print("Mobile No: "+str(i[2]))
					print("Email-ID: "+str(i[3]))
					print("Address: "+str(i[4]))
					print("GST No.: "+str(i[5]))
				print()
		elif option == '2':
			SupplierName = input("Enter Supplier Name: ")
			query="select * from Supplier where Name like '%"+SupplierName+"%';"
			cursor=db.cursor()
			cursor.execute(query)
			data=fetchdetails(cursor)
			if(len(data)==0):
				print("No Supplier with this Name.")
			else:
				for i in data:
					print()
					print("Supplier ID: "+str(i[0]))
					print("Name: "+str(i[1]))
					print("Mobile No: "+str(i[2]))
					print("Email-ID: "+str(i[3]))
					print("Address: "+str(i[4]))
					print("GST No.: "+str(i[5]))
				print()
		elif option == '3':
			clear()
			break
		else :
			print("Enter a valid choice. Try Again")

def View_customer():
	clear()
	while True:
		print("----------------------------- Customer Profile ------------------------------------")
		print("1. Search by Customer ID")
		print("2. Search by Customer Name")
		print("3. Go back")
		option = input("Enter the choice: ")
		if option == '1':
			CustomerID = input("Enter Customer ID: ")
			try:
				CustomerID=int(CustomerID)
			except:
				print("Enter a valid ID. Try Again.")
				continue
			query="select * from Customer where Customer_ID="+str(CustomerID)+";"
			cursor=db.cursor()
			cursor.execute(query)
			data=fetchdetails(cursor)
			if(len(data)==0):
				print("No Customer with this ID.")
			else:
				for i in data:
					print()
					print("Customer ID: "+str(i[0]))
					print("Name: "+str(i[1]))
					print("Mobile No: "+str(i[2]))
					print("Address: "+str(i[3]))
					print("Email-ID: "+str(i[4]))
					print("Credit Card: "+str(i[5]))
				print()
		elif option == '2':
			SupplierName = input("Enter Customer Name: ")
			query="select * from Customer where Name like '%"+CustomerName+"%';"
			cursor=db.cursor()
			cursor.execute(query)
			data=fetchdetails(cursor)
			if(len(data)==0):
				print("No Customer with this Name.")
			else:
				for i in data:
					print()
					print("Customer ID: "+str(i[0]))
					print("Name: "+str(i[1]))
					print("Mobile No: "+str(i[2]))
					print("Address: "+str(i[3]))
					print("Email-ID: "+str(i[4]))
					print("Credit Card: "+str(i[5]))
				print()
		elif option == '3':
			clear()
			break
		else :
			print("Enter a valid choice. Try Again")

def show_stats():
	pass