import numpy as np
from sklearn.linear_model import LinearRegression
import mysql.connector as sql
from datetime import datetime

def fetchdetails(cursor):
	l=[]
	for i in cursor:
		l.append(i)
	return l

def predict_sales_for_item(month,year,Item_ID):
	X=[]
	y=[]
	# now read from database and split the month and year part and add those values in X, and correspoding values of Quantityin y
	db = sql.connect(
		host="localhost",
		user = "root",
		passwd = "himraj18",
		database = "project67"
	)

	cursor=db.cursor()
	query="Select Date, Quantity from prediction where Item_ID="+str(Item_ID)+";"
	cursor.execute(query)
	lst=fetchdetails(cursor)
	ptr=0
	while(ptr<len(lst)):
		date=lst[ptr][0]
		Quantity=int (lst[ptr][1])
		month=int(date.month)
		year=int(date.year)
		ptr+=1
		while(ptr<len(lst)):
			next_date=lst[ptr][0]
			next_month=int(next_date.month)
			next_year=int(next_date.year)
			if(next_month==month and next_year==year):
				Quantity+=int(lst[ptr][1])
				ptr+=1
			else:
				break
		X.append([month,year])
		y.append(Quantity)

	X = np.array(X)
	y = np.array(y)
	reg = LinearRegression().fit(X, y)
	value=reg.predict(np.array([[int(month), int(year)]]))
	return int(value[0])