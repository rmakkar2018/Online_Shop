from global_db import *
from cart import *
from time import sleep

def intersection(lst1, lst2): 
	temp = set(lst2) 
	lst3 = [value for value in lst1 if value in temp]
	return lst3

def searchItem(uid):
	items=[]
	quantity=[]
	while(True):
		_items=[]
		_quantity=[]
		f=True
		clear()
		print("---------------- Searching an Item! -------------------")
		print("Choose one of the options- ")
		print("1. Search by Filters.")
		print("2. Back to Previous Menu")
		s=input("Enter your choice ==> ")
		print()
		# here we search for the particular item's primary key corresponding to the input 
		if(s=='1'):
			item_name=input("Enter Item Name or Press ENTER to skip this Filter - ")
			brand_name=input("Enter Brand Name or Press ENTER to skip this Filter - ")
			dept_name=input("Enter Item Type or Press ENTER to skip this Filter - ")
			offer=input("Press 1 to see items only having offers or press anything - ")
			#print("Offer: "+offer)
			cursor=db.cursor()
			query="Select Item_ID,Name,Company_Name,Price,Available_Quantity from Item where Name like '%"+item_name+"%' and Company_Name like '%"+brand_name+"%' and Department like '%"+dept_name+"%';"
			cursor.execute(query)
			l=fetchdetails(cursor)
			if(len(l)==0):
				print("No Item Available.")
				sleep(2)
				continue
			store=[]
			for i in l:
				store.append(i[0])
			if(offer=='1'):
				query2="Select Item_ID from Offer_Item;"
				cursor.execute(query2)
				l2=fetchdetails(cursor)
				l3=[]
				for i in l2:
					l3.append(i[0])
				#print(l3)
				if(len(l3)==0 or len(intersection(store,l3))==0):
					print("No such Items with Offers available.")
					sleep(2)
					continue
			print('')
			print("Following are Items matching with your search-")
			for i in l:
				if((offer=='1' and i[0] in l3) or offer!='1'):
					print()
					print("Item Number- "+str(i[0]))
					print("Item Name- "+str(i[1]))
					print("Company- "+str(i[2]))
					print("Price- "+str(i[3]))
					print("Available Quantity- "+str(i[4]))
					percentage=fetchoffer(i[0])
					if(percentage>0):
						print("Discount: "+str(percentage)+"%")
			print()
			print("Now enter item number of the items you want to add to your cart along with Quantity")
			print("Enter numbers space seperated like if you want to buy 3 units of item 1")
			print("Then enter '1 3'")
			print("If you don't want to add more items enter -1")
			print()
			while(True):
				try:
					l=list(input().split())
					if(l[0]=='-1'):
						break
					else:
						try:
							l[0]=int(l[0])
							if(l[0] not in store):
								print("Invalid Entry: "+str(l[0]))
								f=False
								break	
						except:
							print("Invalid Entry: "+l[0])
							f=False
							break
						try:
							l[1]=int(l[1])
						except:
							print("Invalid Entry: "+l[1])
							f=False
							break
						if(check_quantity(l[0],l[1])):
							_items.append(l[0])
							_quantity.append(l[1])
						else:
							print("Please enter quantity less than or equal to available quantity.")
							f=False
							break	
				except:
					print("Invalid Entry. Try Again")
					f=False
					break
			if(f and len(_items)>0):
				items=items+_items[:]
				quantity=quantity+_quantity[:]
				print("Items successfully added to cart.")
			else:
				print("Failed to add items to cart due to invalid entry. Please try again.")
		elif(s=='2'):
			clear()
			break
		else:
			print("Please choose one of the options.")
			print()
		print('Press Enter to proceed.')
		garbage=input()
	if(len(items)>0):
		add_to_cart(uid,items,quantity)

def repeatOrder(uid,order_id):
	items=[]
	quantity=[]
	query="Select Item_ID, Quantity from Orders where Order_ID="+str(order_id)+";"
	cursor=db.cursor()
	cursor.execute(query)
	l=fetchdetails(cursor)
	for i in l:
		if(check_quantity(i[0],i[1])):
			items.append(i[0])
			quantity.append(i[1])
		else:
			print()
			print("Unable to add Item-ID: "+str(i[0])+" due to Insufficient Quantity.")
			print("Please add from option Search Items.")
			sleep(2)
	add_to_cart(uid,items,quantity)

def viewPreviousOrder(uid):
	clear()
	query="select Order_ID from cart_order where Cart_ID in (select Cart_Id from customer where Customer_ID="+str(uid)+") order by Order_ID desc;"
	cursor=db.cursor()
	cursor.execute(query)
	l=fetchdetails(cursor)
	if(len(l)==0):
		print("No Previous Orders.")
		sleep(1)
		clear()
		return
	orders=[]
	for i in l:
		orders.append(i[0])
	for i in orders:
		print("Order_ID-"+str(i))
		show_Orders(i)
		fetchbill(i)
	while(True):
		print("Choose one of the options-")
		print("1.Repeat previous order.")
		print("2.Return to previous menu.")
		s=input("Enter your choice ==> ")
		if(s=='1'):
			try:
				x=int(input("Enter Order_ID which you want to repeat ==> "))
			except:
				print('Invalid Option. Please try again.')
				continue
			if(x in orders):
				repeatOrder(uid,x)
				break
			else:
				print('Invalid Option. Please try again.')
				continue
		elif(s=='2'):
			break
		else:
			print('Invalid Option. Please try again.')
			continue

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

def show_items(item_id):
	cursor=db.cursor()
	query="Select Item_ID,Name,Company_Name,Price,Available_Quantity from Item where Item_ID="+str(item_id)+";"
	cursor.execute(query)
	l=fetchdetails(cursor)
	for i in l:
		print("=> Item Number- "+str(i[0]))
		print("=> Item Name- "+str(i[1]))
		print("=> Company- "+str(i[2]))
		print("=> Price- "+str(i[3]))
		print("=> Available Quantity- "+str(i[4]))
		percentage=fetchoffer(i[0])
		if(percentage>0):
			print("=> Discount: "+str(percentage)+"%")
	print()
	return

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
			cmpid=fetch_id()+1
			update_id(cmpid-1,1)
			
			query="Select Mobile_No,Email from Customer where Customer_ID="+str(uid)+";"
			cursor.execute(query)
			details=fetchdetails(cursor)
			#print(details)
			
			query="insert into help_feedback values (%s,%s,%s,%s,%s,%s);"
			values=(cmpid,uid,details[0][0],details[0][1],feedback,False)
			cursor.execute(query,values)
			db.commit()
			
			print('Press Enter to return.')
			garbage=input()
			break
		elif(s=='3'):
			print("Register a complain. Apologies for inconvenience caused.")
			print("Kindly enter all your complain and then press Enter")
			feedback="COMPLAIN: "+input("Complain- ")
			cmpid=fetch_id()+1
			update_id(cmpid-1,1)

			query="Select Mobile_No,Email from Customer where Customer_ID="+str(uid)+";"
			cursor.execute(query)
			details=fetchdetails(cursor)
			#print(details)
			
			query="insert into help_feedback values (%s,%s,%s,%s,%s,%s);"
			values=(cmpid,uid,details[0][0],details[0][1],feedback,False)
			cursor.execute(query,values)
			db.commit()

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
	cursor=db.cursor()
	query="Select * from Customer where Customer_ID="+str(uid)+";"
	cursor.execute(query)
	l=fetchdetails(cursor)
	print("-----------------------------Customer Profile----------------------------")
	for i in l:
		print("=> Customer ID: "+str(i[0]))
		print("=> Name: "+str(i[1]))
		print("=> Mobile No: "+str(i[2]))
		print("=> Address: "+str(i[3]))
		print("=> Email-ID: "+str(i[4]))
		print("=> Credit Card: "+str(i[5]))
	print('Press Enter to return.')
	garbage=input()
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
		# option to add or remove item is not given neither is jump to cart given
		clear()
		print("-----------------------"+"Hello "+str(uid)+"--------------------------");
		print("Choose one of the options-")
		print("1. Search Items")
		print("2. View and Repeat previous Orders")
		print("3. Customer Support or Feedback")
		print("4. View Profile")
		print("5. Go to cart")
		print("6. Logout")
		s=input("Enter your choice ==> ")
		if(s=='1'):
			searchItem(uid)
		elif(s=='2'):
			viewPreviousOrder(uid)
		elif(s=='3'):
			customerSupport(uid)
		elif(s=='4'):
			viewProfile(uid)
		elif(s=='5'):
			if(check_cart(uid)):
				cart_option(uid)
			else:
				print()
				print("No Items in your Cart.")
				sleep(1)
				clear()
		elif(s=='6'):
			if(logout(uid)):
				clear()
				break
			else:
				clear()
		else:
			clear()
			print("Please choose one of the options.")
			sleep(1)

def add_to_cart(uid,items,quantity):
	query1="select Cart_ID from Customer where Customer_ID="+str(uid)+";"
	cursor=db.cursor()
	cursor.execute(query1)
	l=fetchdetails(cursor)
	cart=l[0][0]
	
	query2="insert into cart_item values (%s,%s,%s,%s)"
	for i in range(len(items)):
		query3="select Price from item where Item_ID="+str(items[i])+";"
		cursor.execute(query3)
		price=fetchdetails(cursor)[0][0]

		query4="select count(*) from cart_item where Cart_ID="+str(cart)+" and Item_ID="+str(items[i])+";"
		cursor.execute(query4)
		count=fetchdetails(cursor)[0][0]	
		if(count==0):		
			values=(cart,items[i],quantity[i],price)
			cursor.execute(query2,values)
			db.commit()
		else:
			query5="select Quantity from cart_item where Cart_ID="+str(cart)+" and Item_ID="+str(items[i])+";"
			cursor.execute(query5)
			qq=fetchdetails(cursor)[0][0]
			query6="update cart_item set Quantity="+str(qq+quantity[i])+" where Cart_ID="+str(cart)+" and Item_ID="+str(items[i])+";"
			cursor.execute(query6)
			db.commit()

def check_quantity(item_id,quantity):
	query="select Available_Quantity from Item where Item_ID="+str(item_id)+";"
	cursor=db.cursor()
	cursor.execute(query)
	l=fetchdetails(cursor)
	if(l==0):
		return False
	q=l[0][0]
	if(q<quantity):
		return False
	else:
		av=q-quantity
		query="update Item set Available_Quantity="+str(av)+" where Item_ID="+str(item_id)+";"
		cursor.execute(query)
		db.commit()
		return True
