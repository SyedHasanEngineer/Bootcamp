from ron_addition import add_3
from additional_features import divide_three_numbers
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
print("5. Addition of 3 numbers")
print("6. Division of 3 numbers")

choice = int(input("Enter your choice (1-6): "))
if choice >= 1 and choice < 5:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
elif choice == 5 or choice == 6: 
    num3 = float(input("Enter third number: "))
else:
    print("Error: Invalid choice!")

if choice == 1:
    result = add(num1, num2)
elif choice == 2:
    result = sub(num1, num2)
elif choice == 3:
    result = mul(num1, num2)
elif choice == 4:
    result = div(num1, num2)
elif choice == 5:
    result = add_3(num1, num2, num3)
elif choice == 6:
    result = divide_three_numbers(num1, num2, num3)

else:
    result = "Error: Invalid choice!"

print("Result:", result)