from ron_addition import add_3
from MUL_Imran import mul_3
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
print("6. Multiplication of 3 numbers")

choice = int(input("Enter your choice (1-6): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice==5 or choice==6: 
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
    result = add_3(num1, num2,num3)
elif choice ==6:
    result = mul_3(num1, num2,num3)
else:
    result = "Error: Invalid choice!"

print("Result:", result)