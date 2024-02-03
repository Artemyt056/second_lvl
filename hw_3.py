# task_1
def find_largest_even(lst):
    largest_even = None

    for element in lst:
        if element % 2 == 0:
            if largest_even is None or element > largest_even:
                largest_even = element

    return largest_even


number_list = [1, 4, 7, 2, 9, 10, 6]
largest_even_element = find_largest_even(number_list)
print(largest_even_element)


# task_2
def find_three_max(lst):
    if len(lst) < 3:
        raise ValueError("The list must contain at least three elements")

    sorted_list = sorted(lst, reverse=True)
    max_1, max_2, max_3 = sorted_list[:3]

    return max_1, max_2, max_3


number_list = [1, 10, 4, 13, 22, 10, 0, 105]
max_1, max_2, max_3 = find_three_max(number_list)

print(f"max_1 = {max_1}, max_2 = {max_2}, max_3 = {max_3}")


# task_3
def more_even_elements(list1, list2):
    even_count_list1 = sum(1 for num in list1 if num % 2 == 0)
    odd_count_list2 = sum(1 for num in list2 if num % 2 != 0)

    return even_count_list1 > odd_count_list2


list_1 = [2, 4, 6, 8, 10]
list_2 = [1, 3, 5, 7, 9]

list_3 = [2, 4, 6, 26]
list_4 = [1, 5, 6, 8]

result = more_even_elements(list_1, list_2)
result_2 = more_even_elements(list_3, list_4)
print(result)
print(result_2)
