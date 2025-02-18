def find_common_words(str1, str2):
 
    words1 = set(str1.split())
    words2 = set(str2.split())

   
    common_words = words1.intersection(words2)
    
    return common_words
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
common_words = find_common_words(string1, string2)
print("Common words:", common_words)
