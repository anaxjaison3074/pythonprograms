def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

numbers = [1, 2, 3, 4, 5]
print("Product of the list:", multiply_list(numbers))
