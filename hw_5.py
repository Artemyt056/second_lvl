# task_1
def greatest_common_divisor(x, y):
    if y == 0:
        return x
    else:
        return greatest_common_divisor(y, x % y)


# Example function call
number1 = 48
number2 = 18
result = greatest_common_divisor(number1, number2)
print(f"The greatest common divisor of {number1} and {number2} is {result}")


# task_2
def euclidean_algorithm(a, b):
    if a == 0 or b == 0:
        return [a, b]
    elif a >= 2 * b:
        a = a - 2 * b
        return euclidean_algorithm(a, b)
    elif b >= 2 * a:
        b = b - 2 * a
        return euclidean_algorithm(a, b)
    else:
        return [a, b]


number_a = 20
number_b = 8
result = euclidean_algorithm(number_a, number_b)
print(f"The result of the Euclidean algorithm for {number_a} and {number_b} is {result}")
