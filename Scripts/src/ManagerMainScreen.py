from global_db import *
from datetime import date

def fetch_Customers():
	query="Select Customer_ID,Name from Customer;"
	cursor=db.cursor()
	cursor.execute(query)
	l=fetchdetails(cursor)
	return l

def show_items(item_id):
	cursor=db.cursor()
	query="Select Item_ID,Name,Company_Name,Price,Available_Quantity from Item where Item_ID="+str(item_id)+";"
	cursor.execute(query)
	l=fetchdetails(cursor)
	for i in l:
		print("Item Name- "+str(i[1]))
	print()
	return

def show_Orders(order_id):
	query="select Item_ID from orders where Order_ID="+str(order_id)+";"
	cursor=db.cursor()
	cursor.execute(query)
	l=fetchdetails(cursor)
	items=[]
	for i in l:
		items.append(i[0])
	for i in items:
		show_items(i)

def specificCustomerDetail(x):
	query="select * from Customer where Customer_ID="+str(x)+";"
	cursor=db.cursor()
	cursor.execute(query)
	l=fetchdetails(cursor)
	print("ID- "+str(l[0][0]))
	print("Name- "+str(l[0][1]))
	print("Mobile- "+str(l[0][2]))
	print("Address- "+str(l[0][3]))
	print("Email- "+str(l[0][4]))
	print("Card No- "+str(l[0][5]))
	query="select count(Order_ID) from cart_order where Cart_ID in (select Cart_Id from customer where Customer_ID="+str(x)+") order by Order_ID desc;"
	cursor=db.cursor()
	cursor.execute(query)
	l=fetchdetails(cursor)[0][0]
	print("Total Orders- "+str(l))
	print("Following are the Orders placed by Customer-")
	if(l==0):
		print("No Orders to show.")
	else:
		query="select Order_ID from cart_order where Cart_ID in (select Cart_Id from customer where Customer_ID="+str(x)+") order by Order_ID desc;"
		cursor=db.cursor()
		cursor.execute(query)
		l=fetchdetails(cursor)
		orders=[]
		for i in l:
			orders.append(i[0])
		for i in orders:
			print("Order_ID-"+str(i))
			show_Orders(i)
			fetchbill(i)

def viewCustomers():
	clear()
	customers=fetch_Customers()
	print("----------------------------Customers-----------------------------------")
	while(True):
		print("1. View All Customers.")
		print("2. Search by Customer ID")
		print("3. Exit" )
		s=input("Enter your choice- ")
		if(s=='1'):
			for i in customers:
				print("ID- "+str(i[0])+"\tName- "+str(i[1]))
		elif(s=='2'):
			x=input("Enter Customer ID - ")
			x=int(x)
			f=False
			try:
				for i in customers:
					if(int(x)==i[0]):
						f=True
						break
				if(not f):
					print("No Such Customer.")
				else:
					specificCustomerDetail(x)
			except:
				print("Invalid Customer ID")
		elif(s=='3'):
			clear()
			break
		else:
			print("Invalid Input. Please try again.")

def viewEmployees(uid):
	clear()
	print("----------------------------Employees-----------------------------------")
	query="select * from Employee where Employee_ID in (select Employee_ID from employee_manager where Manager_ID="+str(uid)+");"
	cursor=db.cursor()
	cursor.execute(query)
	l=fetchdetails(cursor)
	for i in l:
		print("Employee_ID- "+str(i[0]))
		print("Name- "+str(i[1]))
		print("Mobile No- "+str(i[2]))
		print("Email- "+str(i[3]))
		print("Address- "+str(i[5]))
		print("Salary- "+str(i[4]))
		print("Hire Date- "+str(i[6]))
		print()

def viewEmployeeAttendance(uid):
	clear()
	print("----------------------------Attendance----------------------------------")
	empid=input("Enter Employee ID- ")
	try:
		empid=int(empid)
	except:
		print("Invalid Employee ID. Please try again.")
		return 
	query="select Employee_ID from Employee where Employee_ID in (select Employee_ID from employee_manager where Manager_ID="+str(uid)+");"
	cursor=db.cursor()
	cursor.execute(query)
	allemp=fetchdetails(cursor)
	f=False
	for i in allemp:
		if(i[0]==empid):
			f=True
			break
	if(f):
		print("Following are the dates when the employee was present-")
		query="select Date from Attendance where Employee_ID="+str(empid)+" and Attendance=1;"
		cursor=db.cursor()
		cursor.execute(query)
		atten=fetchdetails(cursor)
		for i in atten:
			print(i[0])
	else:
		print("Either Invalid Employee ID or this employee is not under you.")

def dbEmployeeRegistration(uid,name,mobile,email,address,salary,password,confPassword):
	id = fetch_id()+1
	hire_date=date.today()
	cursor=db.cursor()
	query="insert into Employee value (%s,%s,%s,%s,%s,%s,%s)"
	value=(id,name,int(mobile),email,float(salary),address,hire_date)
	cursor.execute(query,value)
	db.commit()
	
	query="insert into employee_manager value (%s,%s)"
	value=(id,uid)
	cursor.execute(query,value)
	db.commit()

	query="insert into ID_Pass value (%s,%s)"
	value=(id,password)
	cursor.execute(query,value)
	db.commit()

	update_id(id-1,1)
	return 1

def registerEmployee(uid):
	clear()
	print("---------------------Employee Registration Portal-------------------------")
	print("")
	name  = input("Name : ")
	mobile = input("Mobile No. : ")	
	email = input("Email Id : ")
	address = input("Address : ")
	salary = input("Salary : ")
	password = input("Password : ")
	confPassword = input("Confirm Password : ")
	if(dbEmployeeRegistration(uid,name,mobile,email,address,salary,password,confPassword) == 1):
		print("")
		print("Employee successfully registerd")
		print("")
	else:
		print("")
		print("Employee rgistration failed")
		print("")

def viewProfile(uid):
	clear()
	print("---------------------------Manager Profile-----------------------------------")
	query="Select * from Manager where Manager_ID="+str(uid)+";"
	cursor=db.cursor()
	cursor.execute(query)
	l=fetchdetails(cursor)
	for i in l:
		print("Manager ID- "+str(i[0]))
		print("Name- "+str(i[1]))
		print("Department- "+str(i[3]))
		print("Mobile- "+str(i[7]))
		print("Email- "+str(i[4]))
		print("Address- "+str(i[5]))
		print("Salary- "+str(i[2]))
		print("Hire Date- "+str(i[6]))

def enterManagerMainScreen(uid):
	clear()
	print("--------------------Manager Portal-----------------")
	while (True):
		print("1. View Customers")
		print("2. View Employees")
		print("3. View Employee Attendance")
		print("4. Register Employee")
		print("5. View Profile")
		print("6. Log Out")
		option = input("Enter your choice ==> ")
		if(option =='1'):
			viewCustomers()
		elif(option == '2'):
			viewEmployees(uid)
		elif(option == '3'):
			viewEmployeeAttendance(uid)
		elif(option == '4'):
			registerEmployee(uid)
		elif(option == '5'):
			viewProfile(uid)
		elif(option == '6'):
			clear()
			print("---------------------Login Portal---------------------")
			break
		else:
			print("Enter a valid option")
