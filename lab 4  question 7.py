def find_smallest_word(s):
    
    words = s.split()

    smallest_word = min(words, key=len)
    
    return smallest_word

input_string = input("Enter a string: ")

smallest_word = find_smallest_word(input_string)
print("Smallest word:", smallest_word)




