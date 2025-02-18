def add_ing(input_string):
    if len(input_string) >= 3:
        if input_string.endswith('ing'):
            return input_string + 'ly'
        else:
            return input_string + 'ing'
    return input_string

input_string = "play"
print(add_ing(input_string))

input_string = "playing"
print(add_ing(input_string))

input_string = "go"
print(add_ing(input_string))
