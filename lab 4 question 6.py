def count_vowels(s):
 
    vowels = "aeiou"

    vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    for char in s.lower():
        if char in vowels:
            vowel_count[char] += 1

    return vowel_count

input_string = input("Enter a string: ")

vowel_frequency = count_vowels(input_string)

print("Vowel frequency:", vowel_frequency)
