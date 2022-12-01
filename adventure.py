# "Adventures in Zorkland" player module
def adventure_start():

# LIBRARY LOAD
	from csv import reader
	from csv import DictReader
	from adventure_tavern import adventure_tavern
	import time
	import os

# DATA IMPORT
# Active adventurers header
#	with open("active_adventurers.csv", 'r') as read_obj:
#		csv_dict_reader = DictReader(read_obj)
#		active_adventurers_header = csv_dict_reader.fieldnames

# Current adventurer body only	
	with open("current_adventurer.csv", 'r') as read_obj:
		csv_reader = reader(read_obj)
		current_adventurer = []
		header = next (csv_reader)
		if header != None:
			for row in csv_reader:
				current_adventurer.append(row)

# FUNCTION COLLECTOR
# To create a new adventurer
#def new_adventurer():
	def retire_adventurer():
			with open("retired_adventurers.csv", 'r') as read_obj:
				csv_reader = reader(read_obj)
				retired_adventurers = []
				header = next (csv_reader)
				if header != None:
					for row in csv_reader:
						retired_adventurers.append(row)
			current_adventurer.append(retired_adventurers)
			print(retired_adventurers)
			return

#	with open("valid_users.csv", 'w') as csvfile:
#		writer = csv.writer(csvfile)
#		writer.writerows(valid_users)


# MODULE MENU
# Start menu
	def start_menu():
		hero_name = " "
		if current_adventurer != " ":
			print(" ")
			hero_name = current_adventurer[0][0]
		elif current_adventurer == " ":
			print("No adventurer found...")
			print(current_adventurer)
		selected_user = open('selected_user.txt').read().strip()
		os.system('clear')
		print(f"{selected_user.title()}, welcome to Zorkland!")
		print("\nThis is a land of monsters, treasure, and danger.")
		if hero_name != " ":
			print(f'\n1. Play now with "{hero_name.title()}"')
		elif hero_name == " ":
			print(f"\n1. No active hero.  You'll need to create a new adventurer")
		print("2. Create a new adventurer")
		print(f"3. Retire {hero_name.title()}")
		print("4. Visit retired adventurers")
		print("9. Return to the main menu")
		start_menu1_option = int(input("Enter your choice: "))

# Start menu option logic	
		if start_menu1_option == 1:
			adventure_tavern()
		elif start_menu1_option == 2:
			new_adventurer()
		elif start_menu1_option == 3:
			retire_menu1_option = input(f'Are you sure you want to retire "{hero_name.title}"?\nThis action cannot be undone.\n(y/n):')
			if retire_menu1_option.lower() == 'yes' or 'y':
					retire_adventurer()
			elif retire_menu1_option.lower() == 'no' or 'n':
				start_menu()
		elif start_menu1_option == 4:
			print(" ")
		else:
			start_menu1_option == 9
			print(" ")




