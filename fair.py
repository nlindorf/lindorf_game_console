# "Going to the Fair" player module
def fair_play():

# LIBRARY LOAD
	import csv
	import os
	import time

# DATA IMPORT

# MODULE MENU
# Start menu
	os.system('clear')
	print("Welcome to Zorkland!")
	print("\nThis is a land of monsters, treasure, and danger.")
	print("\n1. I already have an adventurer.")
	print("2. I would like to make my own adventurer.")
	print("3. I would like to see a list of current adventurers.")
	print("4. I would like to retire a current adventurer.")
	print("9. I would like to return to the main menu.")
	menu1_option = int(input("Enter your choice: "))
# Menu option logic	
	if menu1_option == 1:
		menu2_option = input(f"Is {active_adventurers} your current adventurer? y/n\n")
		if menu2_option == "y":
			print("Let your adventure begin!")








	print("Going to the fair.")