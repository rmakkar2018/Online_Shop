from global_db import *
import datetime
from time import sleep

def viewProfile(uid):
	clear()
	print("----------------SUPPLIER PROFILE----------------")
	query="Select * from Supplier where Supplier_ID="+str(uid)+";"
	cursor=db.cursor()
	cursor.execute(query)
	l=fetchdetails(cursor)
	for i in l:
		print("=> Supplier ID: "+str(i[0]))
		print("=> Name: "+str(i[1]))
		print("=> Mobile No: "+str(i[2]))
		print("=> Email-ID: "+str(i[3]))
		print("=> Address: "+str(i[4]))
		print("=> GST No.: "+str(i[5]))
	print('Press Enter to return.')
	garbage=input()

def view_items_supplied(uid):
	while(True):
		clear()
		print("Please choose one of the options.")
		print("1. View all items supplied by you.")
		print("2. Search items supplied by you through filters.")
		print("3. View items having less than 10 units left.")
		print("4. Refill an Item Quantity.")
		print("5. Add new Item.")
		print("6. Back to previous menu.\n")
		s=input("Enter your choice ==> ")
		if(s=='1'):
			clear()
			query="Select Item_ID,Name,Company_Name,Price,Available_Quantity from Item where Item_ID in (select Item_ID from supplier_item where Supplier_ID="+str(uid)+");"
			cursor=db.cursor()
			cursor.execute(query)
			l=fetchdetails(cursor)
			if(len(l)==0):
				print("No Items Supplied by you.")
				sleep(2)
				clear()
				continue
			for i in l:
				print()
				print("=> Item Number- "+str(i[0]))
				print("=> Item Name- "+str(i[1]))
				print("=> Company- "+str(i[2]))
				print("=> Price- "+str(i[3]))
				print("=> Available Quantity- "+str(i[4]))
				print("---------------------------------------------")
			print("Press Enter to Proceed")
			input()
		elif(s=='2'):
			clear()
			print("1. Enter Name or Press ENTER to not to apply this filter.")
			name=input("Name: ")
			print("2. Enter Brand Name or Press ENTER to not to apply this filter.")
			brand_name=input("Brand Name: ")
			print("2. Enter Item Type or Press ENTER to not to apply this filter.")
			item_type=input("Item Type: ")
			query="Select Item_ID,Name,Company_Name,Price,Available_Quantity from Item where Name like '%"+name+"%' and Company_Name like '%"+brand_name+"%' and Department like '%"+item_type+"%' and Item_ID in (select Item_ID from supplier_item where Supplier_ID="+str(uid)+");"
			cursor=db.cursor()
			cursor.execute(query)
			l=fetchdetails(cursor)
			if(len(l)==0):
				print("No such Items Supplied by you.")
				sleep(2)
				clear()
				continue
			for i in l:
				print()
				print("=> Item Number- "+str(i[0]))
				print("=> Item Name- "+str(i[1]))
				print("=> Company- "+str(i[2]))
				print("=> Price- "+str(i[3]))
				print("=> Available Quantity- "+str(i[4]))
				print("---------------------------------------------")
			print("Press Enter to Proceed")
			input()
		elif(s=='3'):
			clear()
			query="Select Item_ID,Name,Company_Name,Price,Available_Quantity from Item where Available_Quantity<10 and Item_ID in (select Item_ID from supplier_item where Supplier_ID="+str(uid)+");"
			cursor=db.cursor()
			cursor.execute(query)
			l=fetchdetails(cursor)
			if(len(l)==0):
				print("No Items Supplied by you is having quantity less than 10.")
				sleep(2)
				clear()
				continue
			for i in l:
				print()
				print("=> Item Number- "+str(i[0]))
				print("=> Item Name- "+str(i[1]))
				print("=> Company- "+str(i[2]))
				print("=> Price- "+str(i[3]))
				print("=> Available Quantity- "+str(i[4]))
				print("---------------------------------------------")
			print("Press Enter to Proceed")
			input()
		elif(s=='4'):
			clear()
			while(True):
				item_id=input("Enter Item ID - ")
				try:
					item_id=int(item_id)
					break
				except:
					print("Please Enter a valid Item ID.")
					continue
			query="select count(*) from Item where Item_ID="+str(item_id)+" and Item_ID in (select Item_ID from supplier_item where Supplier_ID="+str(uid)+");"
			cursor=db.cursor()
			cursor.execute(query)
			l=fetchdetails(cursor)[0][0]
			if(l==0):
				print("Either there is no item with this ID or you haven't delivered this.")
				s=input("Press 1 to try again or Press anything to exit.")
				if(s=='1'):
					continue
				else:
					break
			else:
				query="select Available_Quantity from Item where Item_ID="+str(item_id)+";"
				cursor=db.cursor()
				cursor.execute(query)
				q=fetchdetails(cursor)[0][0]
				while(True):
					av=input("Enter Quantity of new stock- ")
					try:
						av=int(av)
						if(av<=0):
							print("Please Enter a valid Quantity.")
							continue
						break
					except:
						print("Please Enter a valid Quantity.")
						continue
				query="update Item set Available_Quantity="+str(av+q)+" where Item_ID="+str(item_id)+";"
				cursor=db.cursor()
				cursor.execute(query)
				db.commit()
				print("Successfully Refilled.")
				sleep(2)
				clear()
		elif(s=='5'):
			add_new_item(uid)
		elif(s=='6'):
			clear()
			break
		else:
			print("Please choose one of the options.")

def enterSupplierMainScreen(uid):
	while(True):
		clear()
		print("-----------------------"+"Hello "+str(uid)+"--------------------------")
		print("Choose one of the options-")
		print("1. View Items Supplied")
		print("2. Add New Items")
		print("3. View Profile")
		print("4. Logout")
		s=input("Enter your choice ==> ")
		if(s=='1'):
			clear()
			view_items_supplied(uid)
		elif(s=='2'):
			clear()
			add_new_item(uid)
		elif(s=='3'):
			clear()
			viewProfile(uid)
		elif(s=='4'):
			clear()
			if(logout(uid)):
				break
			else:
				clear()
		else:
			clear()
			print("Please choose one of the options.")

def add_new_item(uid):
	clear()
	item_id=fetch_id()+1
	update_id(item_id-1,1);
	print("Item_ID Assigned- "+str(item_id))
	name=input("Item Name- ")
	brand=input("Company Name- ")
	item_type=input("Item Type- ")
	while(True):
		try:
			quantity=int(input("Quantity- "))
			if(quantity<=0):
				print("Invalid Quantity. Must be a number greater than 0.")
				continue
			else:
				break
		except:
			print("Invalid Quantity. Must be a number greater than 0.")
			continue
	while(True):
		try:
			price=float(input("Price- "))
			if(price<=0):
				print("Invalid Price. Must be a number greater than 0.")
				continue
			else:
				break
		except:
			print("Invalid Price. Must be a number greater than 0.")
			continue
	while(True):
		try:
			mfg_date=input("Enter Manufacturing Date (in YYYY-MM-DD format)- ")
			mfg_date=list(map(int,mfg_date.split('-')))
			mfg_date=datetime.datetime(mfg_date[0],mfg_date[1],mfg_date[2])
			break
		except:
			print("Invalid Date. Try Again.")
			continue
	while(True):
		try:
			exp_date=input("Enter Expiry Date (in YYYY-MM-DD format)- ")
			exp_date=list(map(int,exp_date.split('-')))
			exp_date=datetime.datetime(exp_date[0],exp_date[1],exp_date[2])
			break
		except:
			print("Invalid Date. Try Again.")
			continue
	query1="insert into item value (%s,%s,%s,%s,%s,%s,%s,%s);"
	value1=(item_id,name,brand,item_type,price,quantity,mfg_date,exp_date)
	cursor=db.cursor()
	cursor.execute(query1,value1)
	db.commit()
	query2="insert into supplier_item value (%s,%s);"
	value2=(uid,item_id)
	cursor=db.cursor()
	cursor.execute(query2,value2)
	db.commit()
	print("New Item Added Successfully.")
	sleep(2)
	clear()