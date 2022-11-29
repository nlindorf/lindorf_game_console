# This program is a simple calculator.

def calculator():
	import os

	os.system('clear')

# This is the function for addition
	def add(x, y):
		return x + y 

# This is the function for subtraction
	def subtract(x, y):
		return x - y 

# This is the function for multiplication
	def multiply(x, y):
		return x * y 

# This is the function for division
	def divide(x, y):
		return x / y 

# This is a function for exponents
	def exponent(x, y):
		return x ** y 

	print("This is a simple calculator.  \nThese are the available operations: ")

	while True:
# Take input from the user
		print("1. Addition")	
		print("2. Subtraction")
		print("3. Multiply")
		print("4. Divide")
		print("5. Exponent")
		print("9. Quit")
		option = int(input('Enter your choice of operation: '))
		num1 = float(input('Please enter your first number: '))
		num2 = float(input('Please enter your second number: '))
		if option == 1:
			print(num1, "+", num2, "=", add(num1, num2))
			calculator()
		elif option == 2:
			print(num1, "-", num2, "=", subtract(num1, num2))
			time.sleep(2)
			calculator()
		elif option == 3:
			print(num1, "*", num2, "=", multiply(num1, num2))
			calculator()
		elif option == 4:
			print(num1, "/", num2, "=", divide(num1, num2))
			calculator()
		elif option == 5:
			print(num1, "**", num2, "=", exponent(num1, num2))
			calculator()
		elif option == 9:
			print(goodbye_message)
			main_menu()
		else:
			print(invalid_message)
			time.sleep(1)
			calculator()
			
	def next_calculation(): 
		new = input("Would you like to do another calculation? (yes/no): ")
		if new_calculation == "no":
			print("Have a nice day!")
			main_menu()
		elif new_calculation == "yes":
			calculator()
		else:
			print("Invalid Input")
