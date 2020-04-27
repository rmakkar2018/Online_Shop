from global_db import *
from Login import *
from datetime import date

def enterEmployeeMainScreen(uid):
	print("----------------Hello"+uid+"----------------------")
	# he can mark the attendance of that day
	# he can view only his profile
	f=False
	while(True):
		print("")
		print("1. Mark attendance")
		print("2. View Profile")
		print("3. View previous orders")
		print("4. Customer Complaints")
		print("5. Logout")
		option = input("Enter your choice ==> ")
		if(option == '1'):
			markattendance(uid)
		elif(opt
			ion == '2'):
			viewprofile(uid)
		elif(option == '3'):
			view_previous_order()
		elif(option == '4'):
			customer_complaints()
		elif option == '5':
			clear()
			break
		else:
			print("Enter a valid option")

def markattendance(uid):
	# mark the attendance in the attendance table
	clear()
	ddate=date.today()
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	query="select count(*) from Attendance where Employee_ID="+str(uid)+" and Date="+str(ddate)+";"
	cursor=db.cursor()
	cursor.execute(query,value)
	l=fetchdetails(cursor)[0][0]
	if(l==0):
		query="insert into Attendance value (%s,%s,%s,%s)"
		value=(uid,ddate,True,current_time)
		cursor.execute(query,value)
		db.commit()	
		print("Attendance marked.")
		print("Have a good day.")
	else:
		print("Attendance already marked.")

def viewprofile(uid):
	# employee can view only his profile
	clear()
	print("----------------------PROFILE---------------------------")
	query="Select * from Employee where Employee_ID="+str(uid)+";"
	cursor=db.cursor()
	cursor.execute(query)
	l=fetchdetails(cursor)
	for i in l:
		print("Employee ID- "+str(i[0]))
		print("Name- "+str(i[1]))
		print("Mobile- "+str(i[2]))
		print("Email- "+str(i[3]))
		print("Address- "+str(i[5]))
		print("Salary- "+str(i[4]))
		print("Hire Date- "+str(i[6]))
	return

def Specific_order():
	orderID = input(" Enter the order ID of the order to be searched: ")
	#search the order in order table and print the details of the order
	#
	print(" Order found ")

def Search_anyorder():
	print("")
	print("------------------------ Search order -----------------------------")
	while (True):
		print("")
		print("1. Search by CustomerID")
		print("2. Search by Date")
		print("3. Search by itemID")
		print("4. Back to Employee screen")
		option = input("Enter your choice: ")
		if option == '1':
			print("")
			CustomerID = input("Enter the CustomerID: ")
			Search_customerID(CustomerID)
		elif option == '2':
			print("")
			Date = input(" Enter the Date: ")
			Search_date(Date)
		elif option == '3':
			itemID = input(" Enter the itemID: ")
			Search_itemID(itemID)
		elif option=='4':
			clear()
			break
		else:
			print("Enter a valid option")

def Search_customerID(CustomerID):
	#search the ID and return
	print("The order is: ")
	# return

def Search_date(Date):
	# clear()
	print("The order is: ")
	# return

def Search_itemID(itemID):
	# clear()
	print("The order is: ")
	# return 

def view_previous_order():
	# get order details ->given the details of order-> print the details of order
	clear()
	print("")
	print("Get Order Details ")
	#script to get the order details
	print("The details are: ")

def customer_complaints():
	clear()
	compliantID = input(" Enter the compliant ID: ")
	print("The complaint has been resolved.")
	# make the issue variable in the table to true
