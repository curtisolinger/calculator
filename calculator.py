

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

num1 = int(input("What's the first number? "))

for operator in binary_operations:
	print(operator)
operation = input("Pick an operation from the lines above: ")

num2 = int(input("What's the second number? "))

calculation_function = binary_operations[operation]
print(f"{num1} {operation} {num2} = {calculation_function(num1, num2)}")