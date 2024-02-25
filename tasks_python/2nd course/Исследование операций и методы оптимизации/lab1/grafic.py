import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 + 6 * np.exp(0.15*x)

a = -1
b = 0
x = np.linspace(a, b, 100)
y = f(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of the localization interval')
plt.grid(True)
plt.show()