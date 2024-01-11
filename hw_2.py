# exersice №1
some_list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
result = [number for number in some_list1 if number < 5]
print(result)

# exersice №2

ab = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
ba = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_elements = [number for number in ab if number in ba]

print(common_elements)

# exersice №3

arr = [6, 6, 2, 1, 5, 8, 13, 21, 34, 55, 89]
bar = [1, 18, 3, 4, 5, 9, 7, 8, 9, 10, 11, 12, 13]

unique_elements = list(set(number for number in arr if number in bar))

print(unique_elements)