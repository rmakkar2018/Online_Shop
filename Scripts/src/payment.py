def payment_type():
    while (True):
        print("")
        print("1. Pay via Debit or Credit Card")
        print("2. Cash On Delivery")
        print("3. Exit")

        option = int(input("Enter your choice ==> "))
        if (option == 1):
            credit_debit(1234)
        #     go back to home page
        elif (option == 2):
            COD()
        #     go back to home page
        elif (option == 3):
            break
        else:
            print("Enter a valid option")

def COD():
    print("")
    print("Thank for using Online Shop")
    # sql command to track record of cash on delivery

def credit_debit(Cust_ID):
    if(he has credit / debit card):
        show_card(Cust_ID)
        # sql command to show if he / she has credit or Debit card

    else :
        getting_card()
        show_card(Cust_ID)
def getting_card():
    print("")
    name = str(input("Card holder Name : "))
    email = str(input("Bank Name : "))
    mobile = str(input("Type i.e credit or debit : "))
    address = str(input("Expiry Date : "))
    credit_card = int(input("Credit Card No. : "))
    # sql command to add card
    print("Card Added Successfully")


def show_card(CustID):
    print("here we show his credit card/debit card")
    while (True):
        print("")
        print("1. Enter Password to pay")
        print("2. Exit")

        option = int(input("Enter your choice ==> "))
        if (option == 1):
        #     match password with database
            print("Payment successfull")
        elif (option == 2):
            break

        else:
            print("Enter a valid option")
