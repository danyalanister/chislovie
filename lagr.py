def lagrange_interpolation(x_points, y_points, x):
    """
    Интерполяция Лагранжа
    x_points: список значений x
    y_points: список значений y
    x: точка, в которой нужно вычислить значение
    """
    n = len(x_points)
    result = 0.0

    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term

    return result


# Данные из задания 2
x_data = [0.27, 0.93, 1.46, 2.11, 2.87]
y_data = [2.60, 2.43, 2.06, 0.25, -2.60]

# Вычисления для задания 4
print("Задание 4:")
print(f"a) x = 1.02: {lagrange_interpolation(x_data, y_data, 1.02):.4f}")
print(f"б) x = 0.65: {lagrange_interpolation(x_data, y_data, 0.65):.4f}")
print(f"в) x = 1.28: {lagrange_interpolation(x_data, y_data, 1.28):.4f}")


def newton_interpolation(x_points, y_points, x):
    """
    Интерполяция Ньютона
    """
    n = len(x_points)

    # Создаем таблицу разделенных разностей
    fdd = [[0] * n for _ in range(n)]

    # Первый столбец - значения y
    for i in range(n):
        fdd[i][0] = y_points[i]

    # Вычисляем разделенные разности
    for j in range(1, n):
        for i in range(n - j):
            fdd[i][j] = (fdd[i + 1][j - 1] - fdd[i][j - 1]) / (x_points[i + j] - x_points[i])

    # Вычисляем значение интерполяционного многочлена
    result = fdd[0][0]
    product = 1.0

    for i in range(1, n):
        product *= (x - x_points[i - 1])
        result += fdd[0][i] * product

    return result


# Проверка для задания 5
x_data_newton = [1.25, 1.30, 1.35, 1.40, 1.45, 1.50]
y_data_newton = [1.60, 1.71, 1.81, 1.88, 1.94, 1.98]

print("\nЗадание 5 (контрольные точки):")
print(f"x = 1.30: {newton_interpolation(x_data_newton, y_data_newton, 1.30):.4f}")
print(f"x = 1.45: {newton_interpolation(x_data_newton, y_data_newton, 1.45):.4f}")