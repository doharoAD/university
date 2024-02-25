import numpy as np

def f(x):
    return x**2 + 6 * np.exp(0.15*x)

def parabolic_minimization(f, a, b, n):
    for i in range(n):
        x1 = a + (b - a) / 3
        x2 = b - (b - a) / 3

        if f(x1) < f(x2):
            b = x2
        else:
            a = x1

    return (a + b) / 2

a = -1
b = 0
n = 22

min_point = parabolic_minimization(f, a, b, n)
min_value = f(min_point)

print("Точка минимума:")
print(f"x = {min_point}")
print(f"y = {min_value}")