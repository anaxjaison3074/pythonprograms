def count_matching_strings(words):
    count = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count += 1
    return count

sample_list = ['abc', 'xyz', 'aba', '1221']
print("Expected Result:", count_matching_strings(sample_list))
