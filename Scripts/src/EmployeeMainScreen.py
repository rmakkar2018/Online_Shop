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
		print("3. View Orders")
		print("4. View Customer Complaints/Feedbacks")
		print("5. Logout")
		option = input("Enter your choice ==> ")
		if(option == '1'):
			markattendance(uid)
		elif(option == '2'):
			viewprofile(uid)
		elif(option == '3'):
			view_order()
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

def view_order():
	# get order details ->given the details of order-> print the details of order
	clear()
	print("")
	print("Get Order Details ")
	#script to get the order details
	print("The details are: ")

def customer_complaints():
	clear()
	while(True):
		print("If you want to resolve a Complaint/Feedback then visit option 2.")
		print("Choose one of the following-")
		print("1. View all Unresolved Feedback and Complaints.")
		print("2. Detailed view of complaint/feedback by id.")
		print("3. View Resolved Feedback and Complaints.")
		print("4. Feedback and Complaints by a Specific Customer.")
		print("5. Back to Previous Menu.")
		s=input("Enter Choice- ")
		if(s=='1'):
			query="select Complain_ID,Description from help_feedback where Resolved=0;"
			cursor=db.cursor()
			cursor.execute(query)
			l=fetchdetails(cursor)
			for i in l:
				print()
				print("ID- "+str(i[0]))
				print("Description- "+str(i[1]))
			print()
		elif(s=='2'):
			try:
				id=int(input("Enter ID- "))
			except:
				print("Invalid ID. Try Again.")
				continue
			query="select * from help_feedback where complain_id="+str(id)+";"
			cursor=db.cursor()
			cursor.execute(query)
			l=fetchdetails(cursor)
			if(len(l)==0):
				print("Invalid ID. Try Again.")
				continue
			for i in l:
				print()
				print("ID- "+str(i[0]))
				print("CustomerID- "+str(i[1]))
				print("Mobile- "+str(i[2]))
				print("Email- "+str(i[3]))
				print("Description- "+str(i[4]))
				if(i[5]==0):
					print("This is not resolved yet. Press 1 to resolve or any other key.")
					s=input()
					if(s=='1'):
						query="update help_feedback set resolved=1 where id="+str(i[0])+";"
						cursor.execute(query)
						db.commit()
						print("Resolved Now.")
			print()
		elif(s=='3'):
			query="select Complain_ID,Description from help_feedback where Resolved=1;"
			cursor=db.cursor()
			cursor.execute(query)
			l=fetchdetails(cursor)
			for i in l:
				print()
				print("ID- "+str(i[0]))
				print("Description- "+str(i[1]))
			print()
		elif(s=='4'):
			try:
				id=int(input("Enter CustomerID- "))
			except:
				print("Invalid CustomerID.")
				continue
			query="select Complain_ID,Description,Resolved from help_feedback where Customer_ID="+str(id)+";"
			cursor=db.cursor()
			cursor.execute(query)
			l=fetchdetails(cursor)
			for i in l:
				print()
				print("ID- "+str(i[0]))
				print("Description- "+str(i[1]))
				if(i[2]==0):
					print("Not Resolved.")
				else:
					print("Resolved.")
			print()
		elif(s=='5'):
			clear()
			break
		else:
			print("Invalid Choice. Please try again.")
