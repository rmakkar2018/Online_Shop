from payment import *
from OnlineShop import db,get_complain_id,clear
from datetime import datetime

def display_bill(OrderID,total_amount):
    bill_id=6969
    # bill_id is to be fetched
    #
    cursor = db.cursor()
    query = "Insert into bill_orders values( '%" + bill_id + "%','%" + OrderID + "%');"
    cursor.execute(query)

    query = "Insert into bill values('%" + bill_id + "%','%" + total_amount + "%','%" + 0 + "%', '%" + 0 + "%','%" + datetime.date(datetime.now()) + "%','%" + datetime.time(datetime.now()) + "%');"
    cursor.execute(query)

def take_conformation():
    while (True):
        print("")
        print("1. Confirm Order")
        print("2. Exit")

        option = int(input("Enter your choice ==> "))
        if (option == 1):
            print("proceeding to payment portal")
            sleep(1)
            payment_type()
        elif (option == 2):
            break
        else:
            print("Enter a valid option")

