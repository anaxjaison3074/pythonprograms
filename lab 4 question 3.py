def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
my_string = "A man a plan a canal Panama"
if is_palindrome(my_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
