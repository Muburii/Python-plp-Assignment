 #Calculator Program

# Getting the user Input
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
operator = input("Enter an operator(+, -, *, /): ")

#Calculation
if operator == "+":
    result = x + y
    print(f"{x} + {y} = {result}")
elif operator == "-":
    result = x - y
    print(f"{x} - {y} = {result}")
elif operator == "*":
    result = x * y
    print(f"{x} * {y} = {result}")
elif operator == "/":
    if y != 0:
        result = x / y
        print(f"{x} / {y} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")