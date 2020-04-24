from OnlineShop import db,get_comp_id,set_comp_id
from os import system,name

def fetchdetails(cursor):
	l=[]
	for i in cursor:
		l.append(i)
	return l

def clear(): 
	if name == 'nt': 
		_ = system('cls') 
	else: 
		_ = system('clear')

def searchItem(uid):
	while(True):
		clear()
		print("---------------- Searching an Item! -------------------")
		print("Choose one of the options- ")
		print("1. Search by Name")
		print("2. Search by Brand")
		print("3. Search by Deaprtment")
		print("4. Back to Previous Menu")
		s=input("Enter your choice ==> ")
		print()
		# here we search for the particular item's primary key corresponding to the input 
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
			print("")

def repeatOrder(uid):
	clear()

def viewPreviousOrder(uid):
	clear()

def customerSupport(uid):
	clear()
	print("Choose one of the options-")
	while(True):
		print("1. Need Help")
		print("2. Leave a Feedback")
		print("3. Register Complain")
		print("4. Back to Previous Menu")
		s=input("Enter your choice ==> ")
		print()
		cursor=db.cursor()
		if(s=='1'):
			print("Call out Customer Support Executive in case you need Help.")
			print("Call us at +91 8700192939")
			print('Press Enter to return.')
			garbage=input()
			break
		elif(s=='2'):
			print("Leave a feedback. Your feedback is important to us.")
			print("Kindly enter all your feedback and then press Enter")
			feedback="FEEDBACK: "+input("Feedback- ")
			cmpid=get_comp_id()
			set_comp_id(cmpid+1)
			
			query="Select Mobile_No,Email from Customer where Customer_ID="+str(uid)+";"
			cursor.execute(query)
			details=fetchdetails(cursor)
			#print(details)
			
			query="insert into help_feedback values (%s,%s,%s,%s,%s);"
			values=(cmpid,uid,details[0][0],details[0][1],feedback)
			cursor.execute(query,values)
			db.commit()
			
			print('Press Enter to return.')
			garbage=input()
			break
		elif(s=='3'):
			print("Register a complain. Apologies for inconvenience caused.")
			print("Kindly enter all your complain and then press Enter")
			feedback=input("Complain- ")
			
			print('Press Enter to return.')
			garbage=input()
			break
		elif(s=='4'):
			clear()
			break
		else:
			clear()
			print("Please choose one of the options.")

def viewProfile(uid):
	clear()

def logout(uid):
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
	while(True):
		clear()
		print("-----------------------"+"Hello "+uid+"--------------------------");
		print("Choose one of the options-")
		print("1. Search Items")
		print("2. Repeat previous Orders")
		print("3. View previous Orders")
		print("4. Customer Support or Feedback")
		print("5. View Profile")
		print("6. Logout")
		s=input("Enter your choice ==> ")
		if(s=='1'):
			searchItem(uid)
		elif(s=='2'):
			repeatOrder(uid)
		elif(s=='3'):
			viewPreviousOrder(uid)
		elif(s=='4'):
			customerSupport(uid)
		elif(s=='5'):
			viewProfile(uid)
		elif(s=='6'):
			if(logout(uid)):
				break
			else:
				clear()
		else:
			clear()
			print("Please choose one of the options.")