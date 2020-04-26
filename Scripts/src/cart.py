from bill_generator import *
def display_cart(custID , cartID):

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

def cart_option():
    while (True):
        print("")
        print("1. Place Order")
        print("2. Add/Remove Items in Cart")
        print("3. Exit")

        option = int(input("Enter your choice ==> "))
        if (option == 1):
            Place_order()
            display_bill()
            take_conformation()
        elif (option == 2):
            # funtionn to edit items in cart
        elif (option == 3):
            break
        else:
            print("Enter a valid option")

def Place_order():
# sql command to convert add order of cart into order table