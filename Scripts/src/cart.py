from bill_generator import *
from OnlineShop import db,get_complain_id,clear
from os import system,name

def display_cart( cartID):

    print(" ____________________________________________________________________")
    print("| S.No |  Name  | Quantity | cost | Net Cost ")
    cursor = db.cursor()
    query = "Select Name,Quantity,Price from item I , cart_item c where I.Item_ID =c.Item_ID and c.Cart_ID = '%"+cartID+"%';"
    cursor.execute(query)
    l = fetchdetails(cursor)
    Sno = 1
    total_cost=0
    for i in l:
        totalc=float(i[1])*float(i[2])
        print("| "+Sno+" |  "+str(i[0])+"  | "+str(i[1])+" | "+str(i[2])+" |"+totalc)
        print("--------------------------------------------------------------------------------")
        Sno=Sno+1
        total_cost = total_cost +totalc
    print("------------------------------------Total Amount without discount : "+total_cost+"--")
    print("---------------------------------------------------------------------")

def cart_option():
    while (True):
        print("")
        print("1. Place Order")
        print("2. Exit")

        option = input("Enter your choice ==> ")
        if (option == '1'):

            Place_order()
            display_bill()

        elif (option == '2'):
            break
        else:
            clear()
            print("Enter a valid option")

def Place_order(Cust_ID, cart_ID):
#     order  id is to be fetched from a neew table so we have to change this part of hardcode
    order_id=9999;
    cursor = db.cursor()
    query = "Select Item_ID,Quantity,Price from item I , cart_item c where I.Item_ID =c.Item_ID and c.Cart_ID = '%"+cart_ID+"%';"
    cursor.execute(query)
    l = fetchdetails(cursor)

    query = "Insert into cart_order values('%"+cart_ID+"%','%"+order_id+"%');"
    cursor.execute(query)
    for i in l:
        query = "Insert into orders values('%"+order_id+"%','%"+int(i[0])+"%','%"+int(i[1])+"%','%"+float(i[2])+"%');"
        cursor.execute(query)




# sql command to convert add order of cart into order table