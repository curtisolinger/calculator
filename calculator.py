from art import logo


def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	return x / y

binary_operations = {
	"+": add, 
	"-": subtract, 
	"*": multiply, 
	"/": divide,
}

# operator = input("Enter operator: ")
# function = binary_operation[operator]
# print(function(3, 4))

def calculator():

	print(logo)


	num1 = float(input("What's the first number? "))

	for operator in binary_operations:
		print(operator)

	continue_operation = True

	while continue_operation:

		operation = input("Pick an operation from the lines above: ")

		num2 = float(input("What's the second number? "))

		calculation_function = binary_operations[operation]
		answer = calculation_function(num1, num2)


		print(f"{num1} {operation} {num2} = {answer}")

		response = input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation. Type control + c to exit").lower()

		if response == "y":
			num1 = answer
		else:
			continue_operation = False
			calculator()

calculator()

	











