from global_db import *
from datetime import date
from time import sleep
from sales_prediction import predict_sales_for_item

def enterOwnerMainScreen(uid):
	while True:
		clear()
		print(" ----------------------------------- Welcome ----------------------------------")
		print("")
		print("1. Add a new Manager")
		print("2. View People")
		print("3. Show Stats")
		print("4. View Sales Prediction")
		print("5. Logout")
		print("")
		option = input("Enter your choice ==> ")
		if option == '1':
			clear()
			Register_manager();
		elif option == '2':
			clear()
			View()
		elif option == '3':
			clear()
			show_stats()
		elif option == '4':
			try:
				item_id=int(input("Enter Item ID - "))
				month=int(input("Enter Month - "))
				year=int(input("Enter Year - "))
				yyy=date.today().year
				if(1<=month<=12 and year>=yyy):
					pred=predict_sales_for_item(month,year,item_id)
					print()
					print("Predicted Value of sales is "+str(pred))
					print('')
					print('Press ENTER to proceed.')
					g=input()
				else:
					print("Enter valid details.")
					sleep(2)
					continue	
			except:
				print("Enter valid details.")
				sleep(2)
				continue
		elif option == '5':
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
			sleep(2)
			clear()
			return
	except:
		print("Please enter a valid value.")
		print("Registration failed.")
		sleep(2)
		clear()
		return
	department=input("Enter department: ")
	email=input("Enter Email-ID: ")
	if(check(email) == 0):
		print("Enter a valid Email ID")
		sleep(2)
		clear()
		return
	address=input("Enter Address: ")
	try:
		mobile=int(input("Enter Mobile No. : "))
		if(mobile<=0 and len(str(mobile))>10):
			print("Please enter a valid value.")
			print("Registration failed.")
			sleep(2)
			clear()
			return
	except:
		print("Please enter a valid value.")
		print("Registration failed.")
		sleep(2)
		clear()
		return
	hire_date= datetime.date.today()
	password=input("Ënter Password- ")
	cnf_password=input("Confirm password- ")
	if(password!=cnf_password or len(password)==0):
		print("Please enter a valid Password.")
		print("Registration failed.")
		sleep(2)
		clear()
		return
	try:
		query="insert into Manager value (%s,%s,%s,%s,%s,%s,%s,%s);"
		value=(id,name,salary,department,email,address,hire_date,mobile)
		cursor=db.cursor()
		cursor.execute(query,value)
		db.commit()
		query="insert into ID_pass value (%s,%s);"
		value=(id,password)
		cursor = db.cursor()
		cursor.execute(query, value)
		db.commit()
	except:
		print("Registration Failed. Please Try Again.")
		sleep(2)
		clear()
		return
	update_id(id-1,1)
	print()
	print("The Manager has been registered.")
	print("Manager ID- "+str(id))
	print()
	sleep(2)
	clear()

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
		print("2. Search by Manager Name or View all managers")
		print("3. Go back")
		option = input("Enter the choice: ")
		if option == '1':
			ManagerID = input("Enter Manager ID: ")
			try:
				ManagerID=int(ManagerID)
			except:
				print("Enter a valid ID. Try Again.")
			query="select * from Manager where Manager_ID="+str(ManagerID)+";"
			cursor=db.cursor()
			cursor.execute(query)
			data=fetchdetails(cursor)
			if(len(data)==0):
				print("No Manager with this ID.")
				print("Press ENTER to Proceed.")
				garbage=input()
				clear()
				continue
			else:
				for i in data:
					print()
					print("=> Manager ID- "+str(i[0]))
					print("=> Name- "+str(i[1]))
					print("=> Department- "+str(i[3]))
					print("=> Mobile- "+str(i[7]))
					print("=> Email- "+str(i[4]))
					print("=> Address- "+str(i[5]))
					print("=> Salary- "+str(i[2]))
					print("=> Hire Date- "+str(i[6]))
					print()
					print("---------------------------------------------------------------------------")
				print()
				print("Press ENTER to Proceed.")
				garbage=input()
				clear()
		elif option == '2':
			ManagerName = input("Enter Manager Name or Press Enter to view all: ")
			query="select * from Manager where Name like '%"+ManagerName+"%';"
			cursor=db.cursor()
			cursor.execute(query)
			data=fetchdetails(cursor)
			if(ManagerName=='' and len(data)==0):
				print("No Manager Registered yet.")
				print("Press ENTER to Proceed.")
				garbage=input()
				clear()
			elif(len(data)==0):
				print("No Manager with this Name.")
				print("Press ENTER to Proceed.")
				garbage=input()
				clear()
			else:
				for i in data:
					print()
					print("=> Manager ID- "+str(i[0]))
					print("=> Name- "+str(i[1]))
					print("=> Department- "+str(i[3]))
					print("=> Mobile- "+str(i[7]))
					print("=> Email- "+str(i[4]))
					print("=> Address- "+str(i[5]))
					print("=> Salary- "+str(i[2]))
					print("=> Hire Date- "+str(i[6]))
					print()
					print("---------------------------------------------------------------------------")
				print()
				print("Press ENTER to Proceed.")
				garbage=input()
				clear()
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
		print("2. Search by Employee Name or View all Employees")
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
				print("Press ENTER to Proceed.")
				garbage=input()
				clear()
			else:
				for i in data:
					print()
					print("=> Employee ID- "+str(i[0]))
					print("=> Name- "+str(i[1]))
					print("=> Mobile- "+str(i[2]))
					print("=> Email- "+str(i[3]))
					print("=> Address- "+str(i[5]))
					print("=> Salary- "+str(i[4]))
					print("=> Hire Date- "+str(i[6]))
					print()
					print("---------------------------------------------------------------------------")
				print()
				print("Press ENTER to Proceed.")
				garbage=input()
				clear()
		elif option == '2':
			EmployeeName = input("Enter Employee Name or Press Enter to view all: ")
			query="select * from Employee where Name like '%"+EmployeeName+"%';"
			cursor=db.cursor()
			cursor.execute(query)
			data=fetchdetails(cursor)
			if(len(data)==0 and EmployeeName==''):
				print("No Employee Registered yet.")
				print("Press ENTER to Proceed.")
				garbage=input()
				clear()
			elif(len(data)==0):
				print("No Employee with this Name.")
				print("Press ENTER to Proceed.")
				garbage=input()
				clear()
			else:
				for i in data:
					print()
					print("=> Employee ID- "+str(i[0]))
					print("=> Name- "+str(i[1]))
					print("=> Mobile- "+str(i[2]))
					print("=> Email- "+str(i[3]))
					print("=> Address- "+str(i[5]))
					print("=> Salary- "+str(i[4]))
					print("=> Hire Date- "+str(i[6]))
					print()
					print("---------------------------------------------------------------------------")
				print()
				print("Press ENTER to Proceed.")
				garbage=input()
				clear()
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
		print("2. Search by Supplier Name or View All Suppliers")
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
				print("Press ENTER to Proceed.")
				garbage=input()
				clear()
			else:
				for i in data:
					print()
					print("=> Supplier ID: "+str(i[0]))
					print("=> Name: "+str(i[1]))
					print("=> Mobile No: "+str(i[2]))
					print("=> Email-ID: "+str(i[3]))
					print("=> Address: "+str(i[4]))
					print("=> GST No.: "+str(i[5]))
					print()
					print("---------------------------------------------------------------------------")
				print()
				print("Press ENTER to Proceed.")
				garbage=input()
				clear()
		elif option == '2':
			SupplierName = input("Enter Supplier Name or Press Enter for all Supplier: ")
			query="select * from Supplier where Name like '%"+SupplierName+"%';"
			cursor=db.cursor()
			cursor.execute(query)
			data=fetchdetails(cursor)
			if(len(data)==0 and SupplierName==''):
				print("No Supplier registered yet.")
				print("Press ENTER to Proceed.")
				garbage=input()
				clear()
			elif(len(data)==0):
				print("No Supplier with this Name.")
				print("Press ENTER to Proceed.")
				garbage=input()
				clear()
			else:
				for i in data:
					print()
					print("=> Supplier ID: "+str(i[0]))
					print("=> Name: "+str(i[1]))
					print("=> Mobile No: "+str(i[2]))
					print("=> Email-ID: "+str(i[3]))
					print("=> Address: "+str(i[4]))
					print("=> GST No.: "+str(i[5]))
					print()
					print("---------------------------------------------------------------------------")
				print()
				print("Press ENTER to Proceed.")
				garbage=input()
				clear()
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
		print("2. Search by Customer Name or View All Customers")
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
				print("Press ENTER to Proceed.")
				garbage=input()
				clear()
			else:
				for i in data:
					print()
					print("=> Customer ID: "+str(i[0]))
					print("=> Name: "+str(i[1]))
					print("=> Mobile No: "+str(i[2]))
					print("=> Address: "+str(i[3]))
					print("=> Email-ID: "+str(i[4]))
					print("=> Credit Card: "+str(i[5]))
					print()
					print("---------------------------------------------------------------------------")
				print()
				print("Press ENTER to Proceed.")
				garbage=input()
				clear()
		elif option == '2':
			CustomerName = input("Enter Customer Name or Press Enter for all Customers: ")
			query="select * from Customer where Name like '%"+CustomerName+"%';"
			cursor=db.cursor()
			cursor.execute(query)
			data=fetchdetails(cursor)
			if(len(data)==0 and CustomerName==''):
				print("No Customer Registered yet.")
				print("Press ENTER to Proceed.")
				garbage=input()
				clear()
			elif(len(data)==0):
				print("No Customer with this Name.")
				print("Press ENTER to Proceed.")
				garbage=input()
				clear()
			else:
				for i in data:
					print()
					print("=> Customer ID: "+str(i[0]))
					print("=> Name: "+str(i[1]))
					print("=> Mobile No: "+str(i[2]))
					print("=> Address: "+str(i[3]))
					print("=> Email-ID: "+str(i[4]))
					print("=> Credit Card: "+str(i[5]))
					print()
					print("---------------------------------------------------------------------------")
				print()
				print("Press ENTER to Proceed.")
				garbage=input()
				clear()
		elif option == '3':
			clear()
			break
		else :
			print("Enter a valid choice. Try Again")

def show_stats():
	clear()
	query="select count(*) from Manager;"
	cursor=db.cursor()
	cursor.execute(query)
	manager=fetchdetails(cursor)[0][0]

	query="select count(*) from Employee;"
	cursor=db.cursor()
	cursor.execute(query)
	employee=fetchdetails(cursor)[0][0]

	query="select count(*) from Supplier;"
	cursor=db.cursor()
	cursor.execute(query)
	supplier=fetchdetails(cursor)[0][0]

	query="select count(*) from Customer;"
	cursor=db.cursor()
	cursor.execute(query)
	customer=fetchdetails(cursor)[0][0]

	query="select count(Bill_ID) from Bill;"
	cursor=db.cursor()
	cursor.execute(query)
	bills=fetchdetails(cursor)[0][0]

	query="select sum(Total) from Bill;"
	cursor=db.cursor()
	cursor.execute(query)
	earn=fetchdetails(cursor)[0][0]

	if(earn==None):
		earn=0

	print("------------------------- STATISTICS OF SHOP -------------------------")
	print("=> Total Managers- "+str(manager))
	print("=> Total Employee- "+str(employee))
	print("=> Total Supplier- "+str(supplier))
	print("=> Total Customer- "+str(customer))
	print("=> Total Orders- "+str(bills))
	print("=> Total Earnings- "+str(earn))
	print()
	print("Press ENTER to proceed.")
	garbage=input()
	clear()