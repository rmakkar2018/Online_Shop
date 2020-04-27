import mysql.connector as sql
db = sql.connect(
	host="localhost",
	user = "root",
	passwd = "himraj18",
	database = "project67"
)
#populating items using this code

attributes=[]
attributes.append([6,"Travel Bag","American Tourister","Bags",1525.00,15,'2020-03-01',None])
attributes.append([7,"Coca Cola","Coca Cola","Drinks",15.00,250,'2020-04-03','2022-04-03'])
attributes.append([8,"Red Bull","Red Bull","Drinks",105.00,250,'2020-04-03','2022-04-03'])
attributes.append([9,"Pepsi","Pepsi Co","Drinks",20.00,100,'2020-04-03','2022-04-03'])
attributes.append([10,"Blue Pen","Parker","Stationary",250.00,20,'2020-04-03','2022-04-03'])
attributes.append([11,"Black Pen","Cello","Stationary",10.00,69,'2020-04-03','2022-04-03'])
attributes.append([12,"Pencil","Apsara","Stationary",5.00,44,'2020-04-03','2022-04-03'])
attributes.append([13,"Green Chilli Lays","Lays","Chips",10.00,100,'2020-04-03','2022-04-03'])
attributes.append([14,"OREO Biscuit","OREO","Biscuit",25.00,100,'2020-04-03','2022-04-03'])
attributes.append([15,"Cookies","RAVA","Grocery",10.00,1000,'2020-04-03','2022-04-03'])
attributes.append([16,"Volini","Volini","Medical",55.00,100,'2020-04-03','2022-04-03'])
attributes.append([17,"Bandaid","Johnson & Johnson","Medical",5.00,50,'2020-04-03','2022-04-03'])
attributes.append([18,"Adidas Fishcut Shoes","Adidas","Footwear",2500.00,20,'2020-04-03',None])




cursor=db.cursor()
for i in range(len(attributes)):
	attr=attributes[i]
	query="Insert Into item Values (%s,%s,%s,%s,%s,%s,%s,%s);"
	cursor.execute(query,attr)
	db.commit()

#l=fetchdetails(cursor)