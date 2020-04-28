from global_db import *
from payment import *
from datetime import *
def display_cart(cartID):

    print(" ____________________________________________________________________________")
    print('|%6s|%28s|%10s|%12s|%16s|' % ("S.No", "Name", "Quantity", "cost", "Net Cost"))
    print("----------------------------------------------------------------------------")

    #print("| S.No |            Name            | Quantity |    cost    |    Net Cost    |")
    l=list_items_in_cart(cartID)
    Sno = 1
    total_cost=0
    for i in l:
        totalc=float(i[1])*float(i[2])

        print('|%6d|%28s|%10d|%10.2f|%14.2f|'%(Sno,str(i[0]),int(i[1]),float(i[2]),totalc))
        # print("| "+Sno+" |  "+str(i[0])+"  | "+str(i[1])+" | "+str(i[2])+" |"+totalc)
        print("____________________________________________________________________________")
        Sno=Sno+1
        total_cost = total_cost +totalc
    print("|----------------------Total Amount without discount : '%14.2f'------|" %total_cost)
    print("----------------------------------------------------------------------------")

    return total_cost

def cart_option(uid):

    cursor=db.cursor();
    query = "Select Cart_ID from customer where Customer_ID=" + uid + "; "
    cursor.execute(query)
    lst = fetchdetails(cursor)
    cartid = int(lst[0][0])
    while (True):
        clear()
        tc=display_cart(cartid)
        print("")
        print("1. Order Now")
        print("2.Add /Remove Items")
        print("3. Exit")

        option = input("Enter your choice ==> ")
        if (option == '1'):
            while(True):
                clear()
                print("")
                print("1. Confirm Order.")
                print("2. GO back")
                option1 = input("Enter the choice")
                if (option1== '1'):


                    bool=make_payment(uid)
                    if(bool):
                        order_id = Place_order(cartid)

                    break;
                elif(option1=='2'):

                    break;
                else:
                    print("Enter a valid option")

        elif (option == '2'):
            # remove and add items
            clear()


            pass
        elif (option == '3'):
            clear()
            break
        else:
            clear()
            print("Enter a valid option")

def Place_order(cart_ID):
#     order  id is to be fetched from a neew table so we have to change this part of hardcode


    order_id=fetch_id()+1
    cursor = db.cursor()
    query = "Select Item_ID,Quantity,Price from item I , cart_item c where I.Item_ID =c.Item_ID and c.Cart_ID = '%"+cart_ID+"%';"


    # try:
    cursor.execute(query)
    l = fetchdetails(cursor)
    update_id(order_id-1,1)
    print("ID Assigned- " + str(order_id))
    # except:
    #     return 0
    # return 1

    query = "Insert into cart_order values('%"+cart_ID+"%','%"+order_id+"%');"
    cursor.execute(query)
    for i in l:
        query = "Insert into orders values('%"+order_id+"%','%"+int(i[0])+"%','%"+int(i[1])+"%','%"+float(i[2])+"%');"
        cursor.execute(query)

    for i in l:
        query="Select * from prediction where Date="+datetime.date(datetime.now())+"and Item_ID="+int(i[0])+";"
        cursor.execute(query)
        l2=fetchdetails(cursor)
        if(len(l2)==0):
            #we need to insert a row
            query="Insert into prediction values (%s,%s,%s);"
            vales=[datetime.date(datetime.now()),int(i[0]),int(i[1])]
            cursor.execute(query,vales)
            db.commit()
        else:
            #we need to alter the existing row
            query="Update prediction set Quantity ="+(int(l2[0][2]) + int(i[1]))+" where Item_ID = "+int(i[0])+" and Date ="+datetime.date(datetime.now())+";"
            cursor.execute(query)
            db.commit()
    query ="Delete form cart_item where Cart_ID = "+cart_ID+";"
    cursor.execute(query)
    db.commit()

    return order_id

def check_quantity(item_id,quantity):
	query="select Available_Quantity from Item where Item_ID="+str(item_id)+";"
	cursor=db.cursor()
	cursor.execute(query)
	l=fetchdetails(cursor)
	q=l[0][0]
	if(q<quantity):
		return False
	else:
		av=q-quantity
		query="update Item set Available_Quantity="+str(av)+" where Item_ID="+str(item_id)+";"
		cursor.execute(query)
		db.commit()
		return True

def add_or_remove(cart_id):
    cursor=db.cursor()
    while(True):
        clear()
        display_cart(cart_id)
        print("")
        print("1. Add item quantity.")
        print("2. Reduce Item Quantity ")
        print("3. Remove Item")
        print("4. Exit")
        print()
        option = input("Enter the choice")
        if (option == '1'):
            #add item quantity
            clear()
            display_cart(cart_id)
            all_items=list_items_in_cart(cart_id)
            total_items=len(all_items)
            print("Now enter item number of the items you want to add to your cart along with Quantity")
            print("Enter numbers space seperated like if you want to add 3 more units of item 1")
            print("Then enter '1 3'")
            s,q=input().split()
            try:
                if(int(s)<=total_items and int(s)>0 and int(q)>0):
                    #check first the available quantity
                    if(check_quantity(all_items[int(s)-1][3],int(q))):
                        query="update cart_item set Quantity="+str(int(all_items[int(s)-1][2])+int(q))+" where Item_ID="+str(all_items[int(s)-1][3])+"and Cart_ID ="+str(cart_id)+";"
                        cursor.execute(query)
                        db.commit()
                        print("Item added successfully")
                        query="update item set available_Quantity ="+str(get_quantity(all_items[int(s)-1][3])-int(q))+" where Item_ID= "+str(all_items[int(s)-1][3])+";"
                        cursor.execute(query)
                        db.commit()
                        display_cart(cart_id)
                    else:
                        print("Insuffiient Available Quantity left.")
                else:
                    print("enter a valid input next time")
                    print("unsuccessful adding item to cart")
            except:
                print("enter a valid input next time")
                print("unsuccessful adding item to cart")

        elif (option=='2'):
            clear()
            display_cart(cart_id)
            all_items = list_items_in_cart(cart_id)
            total_items = len(all_items)
            print("Now enter item number of the items you want to reduce to your cart along with Quantity")
            print("Enter numbers space seperated like if you want to reduce 3  units of item 1")
            print("Then enter '1 3'")
            s, q = input().split()

            #Reduce item quanity
            try:
                if(int(s)<=total_items and int(s)>0 and int(q)>0 and int(q)<all_items[int(s)-1][2]):
                    #check first the available quantity

                    query="update cart_item set Quantity="+str(int(all_items[int(s)-1][2])-int(q))+" where Item_ID="+str(all_items[int(s)-1][3])+"and Cart_ID ="+str(cart_id)+";"
                    cursor.execute(query)
                    db.commit()
                    print("Item reduce successfully")
                    query="update item set available_Quantity ="+str(get_quantity(all_items[int(s)-1][3])+int(q))+" where Item_ID= "+str(all_items[int(s)-1][3])+";"
                    cursor.execute(query)
                    db.commit()
                    display_cart(cart_id)

                else:
                    print("enter a valid input next time")
                    print("unsuccessful adding item to cart")
            except:
                print("enter a valid input next time")
                print("unsuccessful adding item to cart")

        elif(option=='3'):
            clear()
            display_cart(cart_id)
            all_items = list_items_in_cart(cart_id)
            total_items = len(all_items)
            print("Now enter item number of the items you want to remove from your cart along with Quantity")
            print("Enter item number. If you want to remove item 1")
            print("Then enter '1'")
            s=input()

            try:
                if(int(s)<=total_items and int(s)>0 ):
                    #check first the available quantity
                    query = "update item set available_Quantity =" + str(get_quantity(all_items[int(s) - 1][3]) +(all_items[int(s)-1][2])) + " where Item_ID= " + str(all_items[int(s) - 1][3]) + ";"
                    cursor.execute(query)
                    db.commit()

                    query="delete from cart_item where Item_ID="+str(all_items[int(s)-1][3])+"and Cart_ID ="+str(cart_id)+";"
                    cursor.execute(query)
                    db.commit()
                    print("Item removed successfully")

                    display_cart(cart_id)

                else:
                    print("enter a valid input next time")
                    print("unsuccessful adding item to cart")
            except:
                print("enter a valid input next time")
                print("unsuccessful adding item to cart")


        elif(option=='4'):
            break
        else:
            print("Enter a valid Input")


def get_quantity(item_id):
    query = "select Available_Quantity from Item where Item_ID=" + str(item_id) + ";"
    cursor = db.cursor()
    cursor.execute(query)
    l = fetchdetails(cursor)
    q = l[0][0]
    return q

def list_items_in_cart(cart_id):
    cursor = db.cursor()
    query = "Select I.Name,c.Quantity,c.Price,I.Item_ID from item I , cart_item c where I.Item_ID =c.Item_ID and c.Cart_ID = '%" + str(cart_id) + "%';"
    cursor.execute(query)
    l = fetchdetails(cursor)
    return l;