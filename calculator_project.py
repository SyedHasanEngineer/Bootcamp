def add(a, b):
    return a + b

def add_3(a, b , c):
    return a + b + c  # new feature added

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def mul_3(a, b, c):
    return a * b * c # another feature added

def div(a, b):
    if b == 0:
        return a / b #error fixed 
    else:
        return "Error: Division by zero!"
<<<<<<< Updated upstream

=======
    return a / b
def div3(a, b, c):
    if b == 0:
        return "Error: Division by zero!"
    return a / b / c
>>>>>>> Stashed changes

print("Simple Calculator")
print("1. Addition of 2 numbers")
print("2. Addition of 3 numbers") # New option
print("3. Subtraction of 2 numbers")
print("4. Multiplication of 2 numbers")
print("5. Multipication of 3 numbers")
print("6. Division of 2 numbers")

choice = int(input("Enter your choice (1-7): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = None #about new feature 

#only ask for num3 if needed
if choice in [5, 6, 7]: # error fixed
    num3 = float(input("Enter third number: "))

if choice == 1:
    result = add(num1, num2)
elif choice == 2:
    result = add_3(num1, num2, num3)
elif choice == 3:
    result = sub(num1, num2)
elif choice == 3:
    result = mul(num1, num2)
elif choice == 4:
<<<<<<< Updated upstream
=======
    result = div(num1, num2)
elif choice == 5:
    result = div3(num1, num2, num3) #for new feature
elif choice == 6:
    result = add_3(num1, num2, num3)
elif choice == 7:
>>>>>>> Stashed changes
    result = mul_3(num1, num2, num3)
elif choice == 5:
    result = div(num1, num2)
elif choice == 6:
    result = divide_three_numbers(num1, num2, num3) #for new feature
else:
    result = "Error: Invalid choice!"

print("Result:", result)