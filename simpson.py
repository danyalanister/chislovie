import math


def trapezoidal(f, a, b, n):
    """Метод трапеций"""
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i * h)
    return s * h


def simpson_auto(f, a, b, n=2, eps=1e-6, max_iter=20):
    """
    Метод Симпсона с автоматическим выбором шага.
    Начинает с n (должно быть чётным), удваивает n, пока |S - S_prev| > eps.
    """
    if n % 2 != 0:
        n += 1  # Simpson's rule requires even number of intervals

    S_prev = float('inf')

    for _ in range(max_iter):
        h = (b - a) / n
        S = f(a) + f(b)

        # Odd indices (1, 3, 5, ...)
        for i in range(1, n, 2):
            S += 4 * f(a + i * h)

        # Even indices (2, 4, 6, ..., n-2)
        for i in range(2, n, 2):
            S += 2 * f(a + i * h)

        S = S * h / 3

        if abs(S - S_prev) < eps:
            return S, n

        S_prev = S
        n *= 2  # refine step

    raise RuntimeError("Не удалось достичь заданной точности за максимальное число итераций")


# Пример использования:
if __name__ == "__main__":
    # Интегрируем f(x) = sin(x) от 0 до pi
    f = math.sin
    a, b = 0, math.pi

    # Метод трапеций (с фиксированным n)
    val_trap = trapezoidal(f, a, b, n=1000)

    # Метод Симпсона с автоматическим шагом
    val_simp, n_used = simpson_auto(f, a, b, n=2, eps=1e-8)

    print(f"Точное значение: {2.0}")
    print(f"Трапеции (n=1000): {val_trap:.10f}")
    print(f"Симпсон (n={n_used}): {val_simp:.10f}")