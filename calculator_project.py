from ron_addition import add_3
from Addittional_Sources import mul_3
print("Hello World")
#from new_operations import divide_three_numbers   #new line added

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

print("Simple Calculator")
print("1. Addition of 2 numbers")
print("2. Subtraction of 2 numbers")
print("3. Multiplication of 2 numbers")
print("4. Division of 2 numbers")
print("5. Divide Three Numbers")  # New option
print("6. Addition of 3 numbers")
print("7. Multipication of 3 numbers")

choice = int(input("Enter your choice (1-7): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = None #about new feature 

#only ask for num3 if needed
if choice in [5, 6, 7]: 
    num3 = float(input("Enter third number: "))

if choice == 1:
    result = add(num1, num2)
elif choice == 2:
    result = sub(num1, num2)
elif choice == 3:
    result = mul(num1, num2)
elif choice == 4:
    result = div(num1, num2)
elif choice == 5:
    result = divide_three_numbers(num1, num2, num3) #for new feature
elif choice == 6:
    result = add_3(num1, num2, num3)
elif choice == 7:
    result = mul_3(num1, num2, num3)
else:
    result = "Error: Invalid choice!"

print("Result:", result)