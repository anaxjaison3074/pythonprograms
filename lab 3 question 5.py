num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1 == num2:
    print(f"Two numbers are equal: {num1}")
elif num1 == num3:
    print(f"Two numbers are equal: {num1}")
elif num2 == num3:
    print(f"Two numbers are equal: {num2}")
else:
    print("No two numbers are equal.")
