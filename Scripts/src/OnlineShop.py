from time import sleep
from Login import loginOptions
from SignUp import signUpOptions
from global_db import *
import datetime

def printIntroduction():
	print("***************************************************************")
	print("Welcome to Online Shop")
	print("- An online shopping platform to save the time of the consumers")
	print("- Suggestive shopping methods based on pattern analysis")
	print("***************************************************************")
	print("")
	print("==> Designed by Team-67 (DBMS DEMONS)")
	print("Abhinav Sharma(2018002)")
	print("Himanshu Raj(2018038)")
	print("Rohit Makkar(2018087)")
	print("Jaspreet Saka(2018237)")
	print("Ritik Garg(2018305)")
	print("")
	print("***************************************************************")
	print("")
	print("------------------------Welcome User---------------------------")
	print("")

def aboutApp():
	clear()
	print("The scope of the project is clear to give a simple application to reduce the effort while doing shopping offline or we can say by doing it with an old method.")
	print("In this application, we are trying to save the order list of customers and the customer can repeat any of the previous five orders.")
	print("Trying to provide a hold and pickup service to the customer for their ease.")
	print("***************************************************************************************************************************************************************")
	print("Objectives : ")
	print("1. Convenience")
	print("2. Better Prices")
	print("3. More Variety")
	print("4. Reducing crowds")
	print("5. Repeated Hassle Free orders")
	print("6. Prediction of quantity")
	while(True):
		option = input("Hit 0 to exit : ")
		if(option == "0"):
			clear()
			break

def aboutTeam():
	clear()
	print("******************************************************************")
	print("Team-67 DBMS DEMONS")
	print("1. Abhinav Sharma(2018002)")
	print("2. Himanshu Raj(2018038)")
	print("3. Rohit Makkar(2018087)")
	print("4. Jaspreet Saka(2018237)")
	print("5. Ritik Garg(2018305)")
	while(True):
		option = input("Hit 0 to exit : ")
		if(option == "0"):
			clear()
			break


def exitCredits():
	clear()
	print("")
	print("Thank for using Online Shop")
	print("Hope you have a lovely day.")
	print("Sayonara")

def initOptions():
	while(True):
		print("")
		print("1. Login")
		print("2. Sign Up")
		print("3. About App")
		print("4. About Team-67")
		print("5. Exit")
		option = input("Enter your choice ==> ")
		if(option == '1'):
			loginOptions()
		elif(option == '2'):
			signUpOptions()
		elif(option == '3'):
			aboutApp()
		elif(option == '4'):
			aboutTeam()
		elif(option == '5'):
			exitCredits()
			sleep(2)
			break;
		else:
			print("Enter a valid option")
		clear()
		printIntroduction()
		sleep(0.5)

clear()
printIntroduction()
sleep(0.5)
initOptions()



""" 
the clear function is implemented locally in each file, after each logout the user should jump back to the first screen
so break is added after each action in login type 
"""
