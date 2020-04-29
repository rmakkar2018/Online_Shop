import mysql.connector as sql
from datetime import datetime
from random import *

db = sql.connect(
	host="localhost",
	user = "root",
	passwd = "himraj18",
	database = "project67"
)
cursor=db.cursor()
#populating prediction table using this code

#jan feb march april may june july august sep  oct  nov  dec
# 1   2   3     4     5    6   7     8     9   10    11   12
# 31      28          31       31    31        31         31 

for year in range(2010,2020):
	is_leap_year=False
	if(year%4==0 and year%100!=0):
		is_leap_year=True
	if(year%4==0 and year%100==0 and year%400==0):
		is_leap_year=True

	for month in range(1,13):
		total_no_days=30
		if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
			total_no_days=31
		if(month==2):
			if(is_leap_year):
				total_no_days=29
			else:
				total_no_days=28
		for day in range(1,total_no_days+1):
			today_date=datetime(year,month,day)
			#print(today_date)
			for item_id in range(1005,1018):
				attr=[]
				attr.append(today_date)
				attr.append(item_id)
				sold_num=randint(10,100)
				attr.append(sold_num)
				query="Insert Into prediction Values (%s,%s,%s);"
				cursor.execute(query,attr)
				db.commit()

# for item_id in range(1005,1018):
# 	for month in range(1,13):
# 		base_num=randint(10,100)
# 		for year in range(2010,2020):
# 			is_leap_year=False
# 			if(year%4==0 and year%100!=0):
# 				is_leap_year=True
# 			if(year%4==0 and year%100==0 and year%400==0):
# 				is_leap_year=True


# 			total_no_days=30
# 			if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
# 				total_no_days=31
# 			if(month==2):
# 				if(is_leap_year):
# 					total_no_days=29
# 				else:
# 					total_no_days=28
# 			for day in range(1,total_no_days+1):
# 				today_date=datetime(year,month,day)
# 				attr=[]
# 				attr.append(today_date)
# 				attr.append(item_id)
# 				added_value=randint(0,10)
# 				attr.append(base_num+added_value)
# 				query="Insert Into prediction Values (%s,%s,%s);"
# 				cursor.execute(query,attr)
# 				db.commit()




#the predicted value column has to be removed before using this code