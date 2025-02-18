counter = 0
even_numbers = []

while len(even_numbers) < 4:
    counter += 1
    if counter % 2 != 0:
        continue
    even_numbers.append(counter)

print(even_numbers)
