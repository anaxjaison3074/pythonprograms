def capitalize_first_last(s):
    words = s.split()
 capitalized_words = [
    word[0].upper() + word[1:-1] + word[-1].upper() if len(word) > 1 else word.upper()
        for word in words
    ]
    return " ".join(capitalized_words)
my_string = "hello world from python"
result = capitalize_first
