counter = 0
even_numbers = []

while True:
    if counter % 2 == 0:
        even_numbers.append(counter)
    if len(even_numbers) == 5:
        break
    counter += 1

print(even_numbers)

