import numpy as np

def cubic_spline(x_nodes, y_nodes, x_eval):

    x = np.asarray(x_nodes, dtype=float)
    y = np.asarray(y_nodes, dtype=float)
    if len(x) != len(y):
        raise ValueError("x_nodes and y_nodes must have the same length")
    if len(x) < 2:
        raise ValueError("At least 2 points required")
    if not np.all(np.diff(x) > 0):
        raise ValueError("x_nodes must be strictly increasing")

    n = len(x) - 1  # количество интервалов
    h = np.diff(x)  # h[i] = x[i+1] - x[i], i=0..n-1

    # === Шаг 1: Построение системы для M_i = S''(x_i) ===
    # Естественные условия: M0 = Mn = 0
    # Для внутренних узлов i=1..n-1:
    #   h[i-1] * M[i-1] + 2*(h[i-1]+h[i]) * M[i] + h[i] * M[i+1] = 6 * ((y[i+1]-y[i])/h[i] - (y[i]-y[i-1])/h[i-1])

    if n == 1:
        # Линейная интерполяция (сплайн вырождается)
        def linear_interp(xq):
            t = (xq - x[0]) / h[0]
            return y[0] + t * (y[1] - y[0])
        return np.vectorize(linear_interp)(x_eval)

    # Трёхдиагональная матрица (размер (n-1) × (n-1))
    A = np.zeros((n-1, n-1))
    rhs = np.zeros(n-1)

    for i in range(1, n):  # i = 1 .. n-1 → индекс в M: i, в A: i-1
        idx = i - 1
        if i > 1:
            A[idx, idx-1] = h[i-1]
        A[idx, idx] = 2 * (h[i-1] + h[i])
        if i < n-1:
            A[idx, idx+1] = h[i]

        rhs[idx] = 6 * ( (y[i+1] - y[i]) / h[i] - (y[i] - y[i-1]) / h[i-1] )

    # Решаем A * M_inner = rhs
    M_inner = np.linalg.solve(A, rhs)
    M = np.concatenate(([0.0], M_inner, [0.0]))  # M[0] = M[n] = 0

    # === Шаг 2: Коэффициенты сплайнов на каждом интервале [x_i, x_{i+1}] ===
    # S_i(x) = a_i + b_i*(x - x_i) + c_i*(x - x_i)^2 + d_i*(x - x_i)^3
    a = y[:-1]  # a_i = y_i
    c = M[:-1] / 2  # c_i = M_i / 2
    d = (M[1:] - M[:-1]) / (6 * h)  # d_i = (M_{i+1} - M_i) / (6 * h_i)
    b = (y[1:] - y[:-1]) / h - h * (M[1:] + 2 * M[:-1]) / 6  # b_i

    # === Шаг 3: Интерполяция в точке(ах) x_eval ===
    x_eval = np.asarray(x_eval, dtype=float)
    result = np.empty_like(x_eval)

    for k, xv in enumerate(np.nditer(x_eval)):
        if xv < x[0] or xv > x[-1]:
            # Экстраполяция (линейно, или можно бросить ошибку)
            if xv < x[0]:
                i = 0
            else:
                i = n - 1
        else:
            # Бинарный поиск интервала
            i = np.searchsorted(x, xv) - 1
            i = np.clip(i, 0, n-1)

        dx = xv - x[i]
        result[k] = a[i] + b[i]*dx + c[i]*dx**2 + d[i]*dx**3

    return result if result.shape != () else result.item()


# === Пример использования ===
if __name__ == "__main__":
    # Узлы интерполяции (пример из методички или свой)
    x_nodes = [0, 1, 2, 3]
    y_nodes = [1, 2, 0, 1]

    # Точки для оценки
    x_test = np.linspace(0, 3, 100)
    y_spline = cubic_spline(x_nodes, y_nodes, x_test)

    # Визуализация (если установлен matplotlib)
    try:
        import matplotlib.pyplot as plt
        plt.figure(figsize=(8, 5))
        plt.plot(x_test, y_spline, label='Кубический сплайн', color='blue')
        plt.scatter(x_nodes, y_nodes, color='red', zorder=5, label='Узлы')
        plt.title('Интерполяция кубическим сплайном')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.legend()
        plt.show()
    except ImportError:
        print("matplotlib не установлен. Выводим первые 5 значений:")
        print("x:", x_test[:5])
        print("S(x):", y_spline[:5])