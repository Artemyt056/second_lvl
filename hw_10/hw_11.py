# task_1
is_palindrome = lambda s: s == s[::-1]

print(is_palindrome("level"))
print(is_palindrome("hello"))

# task_2
filter_odd = lambda lst: list(filter(lambda x: x % 2 != 0, lst))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(filter_odd(numbers))

# task_3
filter_by_length = lambda words: list(filter(lambda w: len(w) <= len(words) / len(words), words))

word_list = ["apple", "banana", "orange", "kiwi", "grape"]
print(filter_by_length(word_list))
