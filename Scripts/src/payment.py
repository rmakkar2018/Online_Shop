from payment import *
from OnlineShop import db,get_complain_id,clear

def payment_type():
    while (True):
        print("")
        print("1. Pay via Debit or Credit Card")
        print("2. Exit")

        option = int(input("Enter your choice ==> "))
        if (option == 1):
            credit_debit(1234)
        #     go back to home page
        elif (option == 2):
            break
        else:
            print("Enter a valid option")



def show_card(CustID):
    #print("here we show his credit card/debit card")
    cursor = db.cursor()
    query = "Select Card_ID from customer_card where Customer_ID='%" + CustID + "%';"
    cursor.execute(query)
    l = fetchdetails(cursor)
    options=len(l)
    while (True):
        serial_no = 1;
        for i in l:
            print(serial_no + " " + i[0])
            serial_no + 1
        print("Enter a serial no corresponding to the card u want to choose")
        inp=input();
        try:
            if(int(inp)>options and int(inp)>0):
                continue
        except:
            print("invalid input: ")
            continue

        print("")
        print("1. Enter Password to pay")
        print("2. Exit")

        option = input("Enter your choice ==> ")
        if (option == '1'):
            # match password with database
            print("Enter the CVV")
            inp=input()
            card_id=l[int(inp)][0]
            query = "Select CVV from card_details where Card_ID='%" + card_id + "%';"
            cursor.execute(query)
            l = fetchdetails(cursor)
            password=l[0][0]
            if(password==inp):
                clear()
                print("Payment successfull")
                #now we have to add it to the tables
            else:
                clear()
                print("Wrong CVV....................")
                print("payment cancelled..............")
                sleep(3)
                continue;
        elif (option == '2'):
            break
        else:
            print("Enter a valid option")
