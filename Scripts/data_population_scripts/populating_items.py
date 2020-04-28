import mysql.connector as sql
db = sql.connect(
	host="localhost",
	user = "root",
	passwd = "himraj18",
	database = "project67"
)
#populating items using this code

attributes=[]
attributes.append([1005,"Travel Bag","American Tourister","Bags",1525.00,15,'2020-03-01',None])
attributes.append([1006,"Coca Cola","Coca Cola","Drinks",15.00,250,'2020-04-03','2022-04-03'])
attributes.append([1007,"Red Bull","Red Bull","Drinks",105.00,250,'2020-04-03','2022-04-03'])
attributes.append([1008,"Pepsi","Pepsi Co","Drinks",20.00,100,'2020-04-03','2022-04-03'])
attributes.append([1009,"Blue Pen","Parker","Stationary",250.00,20,'2020-04-03','2022-04-03'])
attributes.append([1010,"Black Pen","Cello","Stationary",10.00,69,'2020-04-03','2022-04-03'])
attributes.append([1011,"Pencil","Apsara","Stationary",5.00,44,'2020-04-03','2022-04-03'])
attributes.append([1012,"Green Chilli Lays","Lays","Chips",10.00,100,'2020-04-03','2022-04-03'])
attributes.append([1013,"OREO Biscuit","OREO","Biscuit",25.00,100,'2020-04-03','2022-04-03'])
attributes.append([1014,"Cookies","RAVA","Grocery",10.00,1000,'2020-04-03','2022-04-03'])
attributes.append([1015,"Volini","Volini","Medical",55.00,100,'2020-04-03','2022-04-03'])
attributes.append([1016,"Bandaid","Johnson & Johnson","Medical",5.00,50,'2020-04-03','2022-04-03'])
attributes.append([1017,"Adidas Fishcut Shoes","Adidas","Footwear",2500.00,20,'2020-04-03',None])

cursor=db.cursor()
for i in range(len(attributes)):
	attr=attributes[i]
	query="Insert Into item Values (%s,%s,%s,%s,%s,%s,%s,%s);"
	cursor.execute(query,attr)
	db.commit()

#l=fetchdetails(cursor)