from os import system,name

def clear(): 
	if name == 'nt': 
		_ = system('cls') 
	else: 
		_ = system('clear') 


def fetchDetails(uid):
	return 1

def showProfileDetails(uid):
	if(fetchDetails(uid) != 1):
		print("Some Unexpected error occured. Try Again Later.")
	
def fetchUpcomingOrders(uid):
	pass
	

		
def printUpcomingOrders():
	clear()
	print("Upcoming Orders")
	print("")
	
def searchOrders(flag,uid):
	clear()
	print("-----------------------Search Orders---------------------")
	while(True):
		print("1. Search by Date")
		print("2. Search by Supplier Name")
		print("3. Search by Item Name")
		print("4. Exit")
		option = input("Enter your choice ==> ")
		if(option == "1"):
			searchbyDate(flag)
		elif(option == "2"):
			searchBySupplierName(flag)
		elif(option == "3"):
			searchByItemName(flag)
		elif(option == "4"):
			break
		else:
			print("Enter a valid option")
			
def getOrderDetails(uid,flag):
	clear()
	print("---------------------------OrderDetails------------------------")
	if(flag == 1):
		printUpcomingOrders()
	else:
		

def showUpcomingOrders(uid):
	if(fetchUpcomingOrders(uid) != 1):
		print("Some Unexpected error occured. Try Again Later.")
	else:
		printUpcomingOrders()
		while(True):
			print("")
			print("1. Print Orders Again")
			print("2. Search Orders")
			print("3. Get Order Details")
			print("4. Exit")
			option = input("Enter your choice ==> ")
			if(option == "1"):
				printUpcomingOrders()
			elif(option == "2"):
				searchOrders(uid,1)
			elif(option == "3"):
				getOrderDetails(uid,1):
			elif(option == "4"):
				break
			else:
				print("Enter a valid option")

def showPreviousOrders(uid):
	if(fetchPreviousOrders(uid) != 1):
		print("Some Unexpected error occured. Try Again Later.")

def enterCustomerProfileMainScreen(uid):
	clear()
	print("-------------------Profile Portal--------------------")
	while(True):
		print("1. Profile Details")
		print("2. Upcoming Orders")
		print("3. Previous Orders")
		print("4. Exit")
		option = input("Enter your choice ==> ")
		if(option == "1"):
			showProfileDetails(uid)
		elif(option == "2"):
			showUpcomingOrders(uid)
		elif(option == "3"):
			showPreviousOrders(uid)
		elif(option == "4"):
			break
		else:
			print("Enter a valid option")
