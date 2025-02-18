number = int (input("Enter a number: "))
if number % 2 == 0:
    result = number ** 2
    print(f"The number is even. The square of {number} is {result}.")
else:
    result = number ** 3
    print(f"The number is odd. The cube of {number} is {result}.")
