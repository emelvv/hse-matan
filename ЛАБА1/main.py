import numpy as np
from scipy.optimize import fsolve

# Определяем функцию
def equation(t):
    numerator = -16 * np.sin(4 * t) + (243 / 2) * np.sin(6 * t) - 225 * np.cos(2 * t) - 150 * np.cos(3 * t) - 350 * np.cos(7 * t) + 900 * np.cos(8 * t)
    return numerator

# Начальные приближения для корней
initial_guesses = np.linspace(0, 2 * np.pi, 10)

# Находим корни
roots = fsolve(equation, initial_guesses)

# Оставляем только уникальные корни в пределах [0, 2*pi]
unique_roots = np.unique(np.round(roots, decimals=5))

# Выводим корни
print(unique_roots)
