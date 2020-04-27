from os import system,name

def clear(): 
	if name == 'nt': 
		_ = system('cls') 
	else: 
		_ = system('clear') 

def viewCustomers():
	print("----------------------------Customers-----------------------------------")

def viewEmployees():
	print("----------------------------Customers-----------------------------------")

def enterManagerMainScreen(uid):
	clear()
	print("--------------------Manager Portal-----------------")
	while (True):
		print("1. View Customers")
		print("2. View Employees")
		print("3. View Orders")
		print("4. View Employee Attendance")
		print("5. Register Employee")
		print("6. View Profile")
		print("7. Log Out")
		option = input("Enter your choice ==> ")
		if(option =='1'):
			viewCustomers()
		elif(option == '2'):
			viewEmployees()
		elif(option == '3'):
			viewOrders()
		elif(option == '4'):
			viewEmployeeAttendance()
		elif(option == '5'):
			registerEmployee(uid)
		elif(option == '6'):
			viewProfile(uid)
		elif(option == '7'):
			clear()
			print("---------------------Login Portal---------------------")
			break
		else:
			print("Enter a valid option")
