import mysql.connector as sql
from os import system,name

db = sql.connect(
	host="localhost",
	user = "root",
	passwd = "himraj18",
	database = "project67"
)

def clear(): 
	if name == 'nt': 
		_ = system('cls') 
	else: 
		_ = system('clear')

def fetchdetails(cursor):
	l=[]
	for i in cursor:
		l.append(i)
	return l

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

def fetch_id():
	query="select ID from ID_Store;"
	cursor=db.cursor()
	cursor.execute(query)
	l=fetchdetails(cursor)[0][0]
	return l

def update_id(id,inc):
	new_id=id+inc
	query="update ID_Store set ID="+str(new_id)+";"
	cursor=db.cursor()
	cursor.execute(query)
	db.commit()

def reg_ID_Pass(id,password):
	query="insert into ID_Pass value (%s,%s);"
	value=(id,password)
	cursor=db.cursor()
	cursor.execute(query,value)
	db.commit()	

def check_valid(id,role):
	if(role=="Owner"):
		if(id==1001 or id=='1001'):
			return True
		else:
			return False
	else:	
		query="select "+str(role)+"_ID from "+str(role)+" where "+str(role)+"_ID="+str(id)+";"
		cursor=db.cursor()
		cursor.execute(query)
		l=fetchdetails(cursor)
		if(len(l)==0):
			return False
		else:
			return True

def fetchoffer(item_id):
	query="select Percentage from Offer where Offer_ID in (select Offer_ID from Offer_Item where Item_ID="+str(item_id)+");"
	cursor=db.cursor()
	cursor.execute(query)
	l=fetchdetails(cursor)
	if(len(l)==0):
		return 0
	else:
		return l[0][0]

def fetchbill(order_id):
	query="select Bill_ID,Created_Time,Created_Date,Total from Bill where Bill_ID in (select Bill_ID from Bill_Orders where Order_ID="+str(order_id)+");"
	cursor=db.cursor()
	cursor.execute(query)
	l=fetchdetails(cursor)
	for i in l:
		print("Date and Time- "+str(i[2])+" "+str(i[1]))
		print("Total Amount- "+str(i[3]))
		