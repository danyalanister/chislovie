import numpy as np
from numpy.polynomial.legendre import leggauss


def gauss2(f, a, b):
    """
    2-точечная формула Гаусса на отрезке [a, b]
    Узлы на [-1,1]: ±1/√3, веса: 1, 1
    """
    # Преобразуем узлы и веса на [a, b]
    t = np.array([-1 / np.sqrt(3), 1 / np.sqrt(3)])
    w = np.array([1.0, 1.0])

    # Аффинное преобразование: x = (b-a)/2 * t + (a+b)/2
    x = 0.5 * (b - a) * t + 0.5 * (a + b)
    fx = np.array([f(xi) for xi in x])

    return 0.5 * (b - a) * np.dot(w, fx)


def gauss3(f, a, b):
    """
    3-точечная формула Гаусса на [a, b]
    Узлы на [-1,1]: 0, ±√(3/5); веса: 8/9, 5/9, 5/9
    """
    t = np.array([-np.sqrt(3 / 5), 0.0, np.sqrt(3 / 5)])
    w = np.array([5 / 9, 8 / 9, 5 / 9])

    x = 0.5 * (b - a) * t + 0.5 * (a + b)
    fx = np.array([f(xi) for xi in x])

    return 0.5 * (b - a) * np.dot(w, fx)


def gauss_legendre(f, a, b, n):
    """
    Обобщённая формула Гаусса–Лежандра с n узлами
    leggauss(n) возвращает узлы и веса на [-1, 1]
    """
    t, w = leggauss(n)  # узлы и веса для [-1, 1]
    x = 0.5 * (b - a) * t + 0.5 * (a + b)
    fx = np.array([f(xi) for xi in x])
    return 0.5 * (b - a) * np.dot(w, fx)


# === Пример из документа ===
# f(x) = 4*x**3
def f(x):
    return 4 * x ** 3


# Точное значение:
I_exact_03 = 3 ** 4 - 0 ** 4  # = 81
I_exact_13 = 3 ** 4 - 1 ** 4  # = 81 - 1 = 80

print("Интеграл ∫ₐᵇ 4x³ dx")
print("-" * 40)
print(f"Точное значение на [0, 3]: {I_exact_03}")
print(f"Точное значение на [1, 3]: {I_exact_13}")
print()

# Вычисления:
for a, b, exact in [(0, 3, I_exact_03), (1, 3, I_exact_13)]:
    print(f"Отрезок [{a}, {b}]:")
    print(f"  2-точечная Гаусс: {gauss2(f, a, b):.10f} (ошибка: {abs(gauss2(f, a, b) - exact):.2e})")
    print(f"  3-точечная Гаусс: {gauss3(f, a, b):.10f} (ошибка: {abs(gauss3(f, a, b) - exact):.2e})")
    print(
        f"  5-точечная Гаусс: {gauss_legendre(f, a, b, 5):.10f} (ошибка: {abs(gauss_legendre(f, a, b, 5) - exact):.2e})")
    print()