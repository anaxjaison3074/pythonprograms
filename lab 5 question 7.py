def string_both_ends(input_string):
    if len(input_string) < 2:
        return ""
    return input_string[:2] + input_string[-2:]

input_string = "Hello"
print(string_both_ends(input_string))
