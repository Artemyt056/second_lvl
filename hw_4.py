def move_zeros(lst):
    non_zeros = [num for num in lst if num != 0 or num is False]
    zeros = [0] * (len(lst) - len(non_zeros))
    result = non_zeros + zeros
    return result


print(move_zeros([False, 1, 0, 1, 2, 0, 1, 3, "a"]))
print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
print(move_zeros([9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))

