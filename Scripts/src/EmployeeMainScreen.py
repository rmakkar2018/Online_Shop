from global_db import *
from Login import *

def enterEmployeeMainScreen(uid):
	print("----------------Hello"+uid+"----------------------")
	# he can mark the attendance of that day
	# he can view only his profile
	while(True):
		print("")
		print("1. Mark attendance")
		print("2. View Profile")
		print("3. View upcoming orders")
		print("4. View previous orders")
		print("5. Customer Complaints")
		print("6. Logout")
		option = input("Enter your choice ==> ")
		if(option == '1'):
			markattendance(uid)
		elif(option == '2'):
			viewprofile(uid)
		elif(option == '3'):
			view_upcoming_order()
		elif(option == '4'):
			view_previous_order()
		elif(option == '5'):
			Customer_complaints()
		elif option == '6':
			clear()
			break
		else:
			print("Enter a valid option")

def markattendance(uid):
	# mark the attendance in the attendance table
	clear()
	#
	print("Attendance marked for uid: " + uid + "\n Have a good day.")


def viewprofile(uid):
	# employee can view only his profile
	clear()
	print("----------------------PROFILE---------------------------")
	#
	return

def view_upcoming_order():
	# search order -> customerID date itemID
	clear()
	#script to print all orders
	while True:
		print("")
		print(" Choose any action ")
		print("1. Get details of any sepcific order")
		print("2. Search any order")
		print("3. Go back")
		option = input(" Enter your choice: ")
		if option == '1':
			Specific_order()
		elif option == '2':
			Search_anyorder()
		elif option == '3':
			clear()
			break
		else:
			print(" Enter a vaild choice: ")

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

def Customer_complaints():
	clear()
	compliantID = input(" Enter the compliant ID: ")
	print("The complaint has been resolved.")
	# make the issue variable in the table to true