import mysql.connector as sql
from os import system,name
import re
from sales_prediction import predict_sales_for_item
import matplotlib.pyplot as plt


db = sql.connect(
	host="localhost",
	user = "root",
	passwd = "himraj18",
	database = "project67"
)

def ret_mobile(s):
	return s[:10]

def clear(): 
	if name == 'nt': 
		_ = system('cls') 
	else: 
		_ = system('clear')

def isInt(string):
	a_low = string.lower()
	if(a_low.islower()):
		return 0
	else:
		return 1	
		
def check(email):
	regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
	if(re.search(regex,email)):
		return 1
	else:
		return 0

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
		print("=> Date and Time- "+str(i[2])+" "+str(i[1]))
		print("=> Total Amount- "+str(i[3]))
		print("---------------------------------------------------")
		
def check_cart(uid):
	query="Select Count(*) from Cart_Item where Cart_ID in (select Cart_ID from Customer where Customer_ID="+str(uid)+");"
	cursor=db.cursor()
	cursor.execute(query)
	l=fetchdetails(cursor)[0][0]
	if(l==0):
		return False
	else:
		return True

def check_cart2(id):
	query="Select Count(*) from Cart_Item where Cart_ID="+str(id)+";"
	cursor=db.cursor()
	cursor.execute(query)
	l=fetchdetails(cursor)[0][0]
	if(l==0):
		return False
	else:
		return True

def check_if_data_present(item_id,month,year):
	query="select count(*) from Prediction where Item_ID="+str(item_id)+" and month(Date)="+str(month)+" and year(Date)="+str(year)+";"
	cursor=db.cursor()
	cursor.execute(query)
	l=fetchdetails(cursor)[0][0]
	if(l==0):
		return False
	else:
		return True	

def collect_data(item_id,month,year):
	query="select sum(Quantity) from Prediction where Item_ID="+str(item_id)+" and month(Date)="+str(month)+" and year(Date)="+str(year)+";"
	cursor=db.cursor()
	cursor.execute(query)
	l=fetchdetails(cursor)[0][0]
	return l

def show_graph(item_id,month,year):
	years_available=[]
	sales_available=[]
	years_pred=[]
	sales_pred=[]
	for i in range(year-4,year+1):
		if(check_if_data_present(item_id,month,i)):
			years_available.append(i)
			val=collect_data(item_id,month,i)
			sales_available.append(val)
		else:
			years_pred.append(i)
			val=predict_sales_for_item(month,i,item_id)
			sales_pred.append(val)
	if(len(years_available)>0):
		years_pred=[years_available[-1]]+years_pred
		sales_pred=[sales_available[-1]]+sales_pred
	plt.plot(years_pred,sales_pred,'--go',label="Predicted Sales")
	if(len(years_available)>0):
		plt.plot(years_available,sales_available,'--bo',label="Previous Sales")
	plt.title("Previous/Predicted Sales of Item ID-"+str(item_id))
	plt.legend()
	plt.xlabel('Year')
	plt.ylabel('Sales in Units')
	plt.xticks(years_available+years_pred)
	plt.show()