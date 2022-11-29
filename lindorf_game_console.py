# Lindorf Game Console, user login and main screen

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
# Function to print main menu
def main_menu():
	os.system('clear')
	print(f"Welcome to the main menu, {selected_user}.")
	print("1. Calculator")
	print("2. Going to the fair")
	print("3. Adventures in Zorkland")
	print("9. Quit")
	option = int(input('Enter your choice: '))
	if option == 1:
		calculator()
		time.sleep(2)
		main_menu()
	elif option== 2:
		fair_play()
		time.sleep(2)
		main_menu()
	elif option == 3:
		adventure_start()
		time.sleep(5)
		main_menu()
	elif option == 9:
		print(goodbye_message)
	else:
		print("Invalid input.  Please try again.")
		time.sleep(1)
		main_menu()

# USER LOGIN
# Messages
username_message = "Please enter your username:"
user_request_message = "Creating a new account now..."
banned_message = ", your account has been banned.  Contact your admin."
login_message = ", signing you in now..."
no_username_message = ", I'm sorry, your account does not exist.  Create an account? (yes/no)"
in_use_message = "is an account that is already in use.  Please try another username."
goodbye_message = "OK.  Have a nice day"

# Logic for sorting out if a valid username is submitted
selected_user = input(username_message)
query_user = list(selected_user.split())
if query_user in banned_users:
		print(selected_user.title() + banned_message)
# Logic for logging in with valid user and creating a home directory
elif query_user in valid_users:
		print(selected_user.title() + login_message)
		directory = selected_user + '_home'
		parent_dir = "/Users/nathanlindorf/desktop/python_work"
		path = os.path.join(parent_dir, directory)
		isExist = os.path.exists(path)
		if isExist == True:
			print(path)
		elif isExist == False:
			os.mkdir(path)
		main_menu()

# Logic for creating a new username
elif query_user not in valid_users:
	if query_user not in banned_users:
		print(selected_user.title() + no_username_message)
		account_creation = input()
		if account_creation == 'yes':
			requested_user = selected_user
			valid_users.append([requested_user])
			with open("valid_users.csv", 'w') as csvfile:
				writer = csv.writer(csvfile)
				writer.writerows(valid_users)
			print(goodbye_message)
		elif account_creation == 'no':
			print(goodbye_message)