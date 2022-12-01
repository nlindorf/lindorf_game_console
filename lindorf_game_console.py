# "Lindorf Game Console" user login and main screen

# LIBRARY LOAD
import csv
import os
from calc import calculator
from fair import fair_play
from adventure import adventure_start
import time

# DATA IMPORT
# Import list of valid usernames
with open("valid_users.csv", 'r') as csvfile:
	rows = csv.reader(csvfile)
	valid_users = []
	for row in rows:
		valid_users.append(row)

# Import list of banned usernames
with open("banned_users.csv", 'r') as csvfile:
	rows = csv.reader(csvfile)
	banned_users = []
	for row in rows:
		banned_users.append(row)

# FUNCTION COLLECTOR

# USER LOGIN
def user_login():

# Storing login user as a static variable
	selected_user = input(username_message)
	active_user = selected_user

# Logic for banned user selection
	query_user = list(selected_user.split())
	if query_user in banned_users:
		print(selected_user.title() + banned_message)
		time.sleep(2)
		user_login()

# Logic for valid user login and creating a home directory
	elif query_user in valid_users:
		print(selected_user.title() + login_message)
		directory = selected_user + '_home'
		parent_dir = "/Users/nathanlindorf/lindorf_game_console/user_home_directories"
		path = os.path.join(parent_dir, directory)
		isExist = os.path.exists(path)
		if isExist == True:
			print(path)
		else:
			isExist == False
			os.mkdir(path)
		writer_text = open(r"selected_user.txt", 'w')
		writer_text.write(active_user)
		writer_text.close()
		main_menu()

# Logic for creating a new username
	elif query_user not in valid_users:
		if query_user not in banned_users:
			print(selected_user.title() + no_username_message)
			account_creation = input()
			if account_creation.lower() == 'yes' or 'y':
				requested_user = selected_user
				valid_users.append([requested_user])
				with open("valid_users.csv", 'w') as csvfile:
					writer = csv.writer(csvfile)
					writer.writerows(valid_users)
				print("User created!")
				user_login()
			else:
				account_creation.lower() == 'no' or 'n'
				print(goodbye_message)

# MAIN MENU
def main_menu():
	os.system('clear')
	print(f"Welcome to the main menu.")
	print("1. Calculator")
	print("2. Going to the fair")
	print("3. Adventures in Zorkland")
	print("9. Quit")
	option = int(input('Enter your choice: '))
	if option == 1:
		calculator()
		main_menu()
	elif option == 2:
		fair_play()
		main_menu()
	elif option == 3:
		adventure_start()
		main_menu()
	elif option == 9:
		print(goodbye_message)
	else:
		print(invalid_message)
		time.sleep(1)
		main_menu()


# Messages
username_message = "Please enter your username:"
user_request_message = "Creating a new account now..."
banned_message = ", your account has been banned.  Contact your admin."
login_message = ", signing you in now..."
no_username_message = ", I'm sorry, your account does not exist.  Create an account? (yes/no)"
in_use_message = "is an account that is already in use.  Please try another username."
goodbye_message = "OK.  Have a nice day"
invalid_message = "Invalid input.  Please try again."

user_login()