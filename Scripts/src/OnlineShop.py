from os import system,name
from time import sleep
from Login import *
from SignUp import *

def clear(): 
	if name == 'nt': 
		_ = system('cls') 
	else: 
		_ = system('clear') 

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
	print("Ritik Garg(2018307)")
	print("")
	print("***************************************************************")
	print("")
	print("------------------------Welcome User---------------------------")
	print("")

def aboutApp():
	clear()

def exitCredits():
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
		print("4. Exit")
		option = input("Enter your choice ==> ")
		if(option == '1'):
			loginOptions()
		elif(option == '2'):
			signUpOptions()
		elif(option == '3'):
			aboutApp()
		elif(option == '4'):
			exitCredits()
			break;
		else:
			print("Enter a valid option")

if __name__ == '__main__':
	clear()
	printIntroduction()
	sleep(2)
	initOptions()