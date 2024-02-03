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

arr = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

bar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []

for i in range(len(arr)):

    for j in range(len(bar)):

        if not arr[i] == bar[j]:
            c.append(arr[i])

print(list(set(sorted(c))))
