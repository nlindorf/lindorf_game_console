# Adventures in Zorkland player module

# LIBRARY LOAD
def adventure_start():
	from csv import reader
	from csv import DictReader
	from adventure_tavern import adventure_tavern
	import time
	import os

# UNIVERSAL VARIABLES
	#home_dir = nathan_home
	#home_path = "/Users/nathanlindorf/desktop/python_work" + home_dir
	#sys_path = "/Users/nathanlindorf/desktop/python_work"
# DATA IMPORT
# Active adventurers header
	with open("active_adventurers.csv", 'r') as read_obj:
		csv_dict_reader = DictReader(read_obj)
		active_adventurers_header = csv_dict_reader.fieldnames

# Active adventurers body	
	with open("active_adventurers.csv", 'r') as read_obj:
		csv_reader = reader(read_obj)
		active_adventurers = []
		header = next (csv_reader)
		if header != None:
			for row in csv_reader:
				active_adventurers.append(row)


# Adventure start menu
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
			#src = sys_path + 'active_adventurers.csv'
			#dst = home_path + 'active_adventurers.csv'
			#os.system(f"cp {src} {dst}")
			time.sleep(4)
			adventure_tavern()





