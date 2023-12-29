# exersice №1
some_list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
result = [number for number in some_list1 if number < 5]
print(result)

# exersice №2

some_list2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
some_list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result = list(set(some_list2) and set(some_list3))
print(result)

# exersice №3

some_list4 = [6, 6, 2, 1, 5, 8, 13, 21, 34, 55, 89]
some_list5 = [1, 18, 3, 4, 5, 9, 7, 8, 9, 10, 11, 12, 13]
result = list(set(some_list4 + some_list5))
print(result)
