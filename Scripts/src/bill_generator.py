from payment import *
def display_bill(OrderID , Bill_ID):

    print("_________________________________Store_Name-----------------------")
    print("Name :" )
    print("Contact No. : ")
    print("Date : and time:")
    print(" ____________________________________________________________________")
    print("| S.No |  Name  | Quantity | cost | Net Cost | Discount | Total cost |")
    while(True):
        Sno= 0
        Total_cost =0
        print("| Sno |  Name  | Quantity | cost |cost * Quantity | Discount | Net - Discount |")
        print("--------------------------------------------------------------------------------")
        Sno=Sno+1
        Total_cost = total_cost +Total_cost
    print("-----------------------------------------------------Total Amount : Total_cost--")
    print("--------------------------------------------------------------------------------")

def take_conformation():
    while (True):
        print("")
        print("1. Confirm Order")
        print("2. Exit")

        option = int(input("Enter your choice ==> "))
        if (option == 1):
            print("proceeding to payment portal")
            payment_type()
        elif (option == 2):
            break
        else:
            print("Enter a valid option")

