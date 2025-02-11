def find_smallest(numbers):
    smallest = numbers[0]  
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

numbers = [10, 25, 3, 99, 56]
print("Smallest number in the list:", find_smallest(numbers))
