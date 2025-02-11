def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

numbers = [10, 25, 3, 99, 56]
print("Largest number in the list:", find_largest(numbers))
