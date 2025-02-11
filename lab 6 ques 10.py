def words_longer_than_n(words, n):
    return [word for word in words if len(word) > n]

word_list = ['apple', 'banana', 'cherry', 'date', 'kiwi']
n = 5
long_words = words_longer_than_n(word_list, n)

print(f"Words longer than {n} characters:", long_words)
