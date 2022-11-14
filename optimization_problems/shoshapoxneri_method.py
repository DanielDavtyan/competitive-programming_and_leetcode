from math import exp as e, sqrt
from numpy import arange


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def passive_method(math_function, range_of_x_axis: list, accuracy: float) -> float:
    length = range_of_x_axis[0] - range_of_x_axis[1]
    k = length / accuracy
    step = length / k
    function_values = [math_function(value) for value in arange(range_of_x_axis[0], range_of_x_axis[1], step)]
    return min(function_values)


def divide_method(math_function, range_of_x_axis: list, accuracy: float, delta: float = 0.1) -> float:
    a = range_of_x_axis[0]
    b = range_of_x_axis[1]

    while not ((b - a) / 2 <= accuracy):
        c = (a + b) / 2 - delta / 2
        d = (a + b) / 2 + delta / 2
        if math_function(c) <= math_function(d):
            b = d
        else:
            a = c
    return math_function((a + b) / 2)


def golden_medium_method(math_function, range_of_x_axis: list, accuracy: float) -> float:
    a = range_of_x_axis[0]
    b = range_of_x_axis[1]
    i = 1
    while not ((b - a) / 2) <= accuracy:
        c = ((3 - sqrt(5)) / 2) * (b - a) + a
        d = ((sqrt(5) - 1) / 2) * (b - a) + a
        if math_function(c) <= math_function(d):
            b = d
            d = c
            c = ((3 - sqrt(5)) / 2) * (b - a) + a
        else:
            a = c
            c = d
            d = ((sqrt(5) - 1) / 2) * (b - a) + a
        accuracy = 0.5 * (((sqrt(5) - 1) / 2) ** (i - 1)) * (b - a)
        i += 1
    return math_function((a + b) / 2)


def fibonacci_method(math_function, range_of_x_axis: list, accuracy: float) -> float:
    a = range_of_x_axis[0]
    b = range_of_x_axis[1]
    number_for_see_iterations = (b - a) / accuracy
    i = 1
    while True:
        value = fibonacci(i)
        if value >= number_for_see_iterations:
            break
        i += 1
    steps = i - 2
    for step in range(steps):
        c = a + (b - a) * (fibonacci(step) / fibonacci(step + 2))
        d = a + (b - a) * (fibonacci(step + 1) / fibonacci(step + 2))
        if math_function(c) <= math_function(d):
            b = d
            d = c
        else:
            a = c
            c = d
    return math_function((a + b) / 2)


def current_function(x):
    if 0 <= x <= 0.45:
        return -1 * e(3 * x / 2)
    elif 0.45 <= x <= 0.7:
        return 2.3 * x - 3
    elif 0.7 <= x <= 1:
        return (x ** 2) - 1
    else:
        print("please provide x in [0, 1] range")


def func(x):
    return (x + 2) / x


print(passive_method(current_function, [0, 1], 0.01))
print(divide_method(current_function, [0, 1], 0.01, 0.01))
print(golden_medium_method(current_function, [0, 1], 0.01))
print(fibonacci_method(current_function, [0, 1], 0.01))
