import numpy as np
from numpy.linalg import norm, inv

A = np.array([[4, 1], [1, 5]])
# A = np.array([[4, 1], [1, 6]])

x = np.array([1, 1])
b = np.array([1, 0])
epsilon = 0.01


# Our function is f(x) = 1/2 * (Ax, b) + (b, x), Derivative of this function is f'(x) = Ax + b,
# for further gradient calculations we will use derivative function.

def current_function_derivative(x):
    return np.dot(A, x) + b


def apfa_k_calculation(function, x_k):
    return (norm(function(x_k), 1) ** 2) / np.dot(np.dot(A, function(x_k)), function(x_k))


def x_k_calculation(function, previous_x_k, alfa_k_1):
    return previous_x_k - np.dot(alfa_k_1, function(previous_x_k))


step = 0
while not norm(current_function_derivative(x)) <= epsilon:
    alfa_k = apfa_k_calculation(current_function_derivative, x)
    x = x_k_calculation(current_function_derivative, x, alfa_k)
    print(x)
    step += 1

print(np.dot(-1 * inv(A), b), 10 * "*")
print(step, x)
