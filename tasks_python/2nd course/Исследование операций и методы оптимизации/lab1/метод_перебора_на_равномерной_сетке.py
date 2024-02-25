import numpy as np

# Определить функцию
def f(x):
    return (x**2) + 6 * np.exp(0.15 * x)

# Определить отрезок
a = -1
b = 0

# Определить число итераций
n = 22

# Создать массив значений x
x = np.linspace(a, b, n)

# Вычислить значения y
y = f(x)

# Найти точку минимума
min_index = np.argmin(y)
min_x = x[min_index]
min_y = y[min_index]

# Вывести результат на экран
print("Точка минимума:")
print("x =", min_x)
print("y =", min_y)