def replace_char(input_string):
    first_char = input_string[0]
    modified_string = first_char + input_string[1:].replace(first_char, '$')
    return modified_string

input_string = "restart"
print(replace_char(input_string))
