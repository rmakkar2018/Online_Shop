from payment import *
from global_db import *

def make_payment(CustID):
	#print("here we show his credit card/debit card")
	done_payment=False
	cursor = db.cursor()
	query = "Select Credit from customer where Customer_ID="+str(CustID)+";"
	cursor.execute(query)
	l = fetchdetails(cursor)[0][0]
	while(done_payment!=True):
		print("Card No.- "+str(l))
		print("If you want to use the above card then press 1 else press anything.")
		s=input()
		if(s!='1'):
			while(True):
				try:
					l=int(input())
					break
				except:
					print("Enter valid Card No.")
		print("")
		print("1. Enter CVV to pay")
		print("2. Exit")

		option = input("Enter your choice ==> ")
		if (option == '1'):
			# match password with database
			print("Enter the CVV.")
			while(True):
				try:
					cvv=int(input())
					break
				except:
					print("Enter valid CVV.")
					continue
			print("Payment successfull.")
			done_payment=True
		elif (option == '2'):
			break
		else:
			print("Enter a valid option")
	return done_payment