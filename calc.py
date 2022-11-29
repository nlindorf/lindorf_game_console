# This program is a simple calculator.
def calculator():

#LIBRARY LOAD
	import os
	import time

# FUNCTION COLLECTOR
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

# This is a function for processing post calculation
	def next_calculation():
		while True: 
			input("Press any key to return to calculator menu: ")
			break

#USER MENU
	while True:
		os.system('clear')
		print("This is a simple calculator.  \nThese are the available operations: ")
	
# Take input from the user
		print("1. Addition")	
		print("2. Subtraction")
		print("3. Multiply")
		print("4. Divide")
		print("5. Exponent")
		print("9. Quit")
		option = int(input('Enter your choice of operation: '))
		if option == 9:
			break
		else:
			num1 = int(input('Please enter your first number: '))
			num2 = int(input('Please enter your second number: '))
		if option == 1:
			print(num1, "+", num2, "=", add(num1, num2))
			next_calculation()
		elif option == 2:
			print(num1, "-", num2, "=", subtract(num1, num2))
			next_calculation()
		elif option == 3:
			print(num1, "*", num2, "=", multiply(num1, num2))
			next_calculation()
		elif option == 4:
			print(num1, "/", num2, "=", divide(num1, num2))
			next_calculation()
		elif option == 5:
			print(num1, "**", num2, "=", exponent(num1, num2))
			next_calculation()
		elif option == 9:
			break
		else:
			print("Invalid input.  Please try again.")
			time.sleep(1)
			calculator()
