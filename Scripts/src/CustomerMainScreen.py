from OnlineShop import *;

def searchItem():
	clear()
	print("Choose one of the options-")
	while(True):
		print("1. Search by Name")
		print("2. Search by Brand")
		print("3. Search by Deaprtment")
		print("4. Back to Previous Menu")
		s=input("Enter your choice ==> ")
		print()
		if(s=='1'):
			pass
		elif(s=='2'):
			pass
		elif(s=='3'):
			pass
		elif(s=='4'):
			clear()
			break
		else:
			clear()
			print("Please choose one of the options.")

def repeatOrder():
	clear()

def viewPreviousOrder():
	clear()

def customerSupport():
	clear()
	print("Choose one of the options-")
	while(True):
		print("1. Need Help")
		print("2. Leave a Feedback")
		print("3. Register Complain")
		print("4. Back to Previous Menu")
		s=input("Enter your choice ==> ")
		print()
		if(s=='1'):
			print("Call out Customer Support Executive in case you need Help.")
			print("Call us at +91 8700192939")
		elif(s=='2'):
			print("Leave a feedback. Your feedback is important to us.")
			print("Kindly enter all your feedback and then press Enter")
			feedback=input("Feedback- ")
		elif(s=='3'):
			print("Register a complain. Apologies for inconvenience caused.")
			print("Kindly enter all your complain and then press Enter")
			feedback=input("Complain- ")
		elif(s=='4'):
			clear()
			break
		else:
			clear()
			print("Please choose one of the options.")

def viewProfile():
	clear()

def logout():
	while(True):
		print("Do you want to logout?(Y/N)")
		s=input()
		if(s=='Y'):
			return True
		elif(s=='N'):
			return False
		else:
			clear()
			print("Please choose Y/N.")

def enterCustomerMainScreen(uid):
	print("Hello "+uid);
	while(True):
		print("Choose one of the options-")
		print("1. Search Items")
		print("2. Repeat previous Orders")
		print("3. View previous Orders")
		print("4. Customer Support or Feedback")
		print("5. View Profile")
		print("6. Logout")
		s=input("Enter your choice ==> ")
		if(s=='1'):
			searchItem()
		elif(s=='2'):
			repeatOrder()
		elif(s=='3'):
			viewPreviousOrder()
		elif(s=='4'):
			customerSupport()
		elif(s=='5'):
			viewProfile()
		elif(s=='6'):
			if(logout()):
				break
			else:
				clear()
		else:
			clear()
			print("Please choose one of the options.")