from global_db import *

#populating items using this code

attributes=[]

attributes.append([1,"OREO Biscuit","OREO",25.00,100,'01-03-2020','01-12-2020'])
attributes.append([2,"Cookies","RAVA",10.00,1000,'02-01-2020','02-10-2020'])
attributes.append([3,"Volini","Volini",55.00,100,'05-06-2020','05-12-2020'])
attributes.append([4,"Bandaid","Johnson & Johnson",5.00,50,'12-02-2020','12-10-2020'])
attributes.append([5,"Adidas Fishcut Shoes","Adidas",2500.00,20,'01-03-2020',None])
attributes.append([6,"Travel Bag","American Tourister",1525.00,15,'01-03-2020',None])
attributes.append([7,"Coca Cola","Coca Cola",15.00,250,'03-04-2020','03-07-2020'])
attributes.append([8,"Red Bull","Red Bull",105.00,250,'04-04-2020','04-08-2020'])
attributes.append([9,"Pepsi","Pepsi Co",20.00,100,'13-03-2020','13-06-2020'])
attributes.append([10,"Blue Pen","Parker",250.00,20,'12-01-2020','12-12-2020'])
attributes.append([11,"Black Pen","Cello",10.00,69,'01-04-2020','01-03-2021'])
attributes.append([12,"Pencil","Apsara",5.00,44,'23-02-2020','23-12-2020'])
attributes.append([13,"Green Chilli Lays","Lays",10.00,100,'25-01-2020','25-07-2020'])





cursor=db.cursor()
for i in range(len(attributes)):
	attr=attributes[i]
	query="Insert Into item Values ("+str(attr[0])+"," +str(attr[1])+"," +str(attr[2])+"," +str(attr[3])+"," +str(attr[4])+"," +str(attr[5])+"," +str(attr[6])+","  ");"
	cursor.execute(query)

#l=fetchdetails(cursor)
