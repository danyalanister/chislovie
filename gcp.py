import math


def euler_method(f, x0, y0, h, n):
    """Метод Эйлера"""
    x = x0
    y = y0
    results = [(x, y)]
    for i in range(n):
        y = y + h * f(x, y)
        x = x + h
        results.append((x, y))
    return results


def euler_koshi_method(f, x0, y0, h, n):
    """Метод Эйлера-Коши (улучшенный метод Эйлера)"""
    x = x0
    y = y0
    results = [(x, y)]
    for i in range(n):
        # Предиктор (метод Эйлера)
        y_pred = y + h * f(x, y)
        x_next = x + h
        # Корректор (среднее арифметическое)
        y = y + (h / 2) * (f(x, y) + f(x_next, y_pred))
        x = x_next
        results.append((x, y))
    return results


def runge_kutta_4_method(f, x0, y0, h, n):
    """Метод Рунге-Кутта 4-го порядка"""
    x = x0
    y = y0
    results = [(x, y)]
    for i in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h / 2, y + k2 / 2)
        k4 = h * f(x + h, y + k3)
        y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x = x + h
        results.append((x, y))
    return results


def exact_solution(x):
    """Точное решение для y' = y - x^2 + 1, y(0)=0.5"""
    return (x ** 2 + 2 * x + 2) - 1.5 * math.exp(x)


def print_results(method_name, results, exact_func=None):
    """Вывод результатов с точным решением, если доступно"""
    print(f"\n{method_name}:")
    print(f"{'x':>8} {'y':>12} {'Точное значение':>15} {'Погрешность':>12}")
    print("-" * 60)
    for x, y in results:
        if exact_func:
            exact_y = exact_func(x)
            error = abs(y - exact_y)
            print(f"{x:8.4f} {y:12.6f} {exact_y:15.6f} {error:12.6f}")
        else:
            print(f"{x:8.4f} {y:12.6f}")


def main():
    print("=== Решение ОДУ ===")

    # Определение функции f(x, y) для ОДУ y' = f(x, y)
    # Уравнение из 25 слайда: y' = y - x^2 + 1
    def f(x, y):
        return y - x ** 2 + 1

    # Начальные условия
    x0 = 0.0
    y0 = 0.5
    x_end = 2.0
    n = 10  # Количество шагов (можно изменить)
    h = (x_end - x0) / n

    while True:
        print("\nВыберите метод:")
        print("1. Блок-схема метода Эйлера (10 слайд)")
        print("2. Блок-схема метода Эйлера – Коши (14 слайд)")
        print("3. Блок-схема метода Рунге-Кутта 4 порядка (16 слайд)")
        print("4. Проверить на ОДУ 25 слайд (y' = y - x^2 + 1, y(0)=0.5)")
        print("5. Выход")

        choice = input("Введите номер: ").strip()

        if choice == '1':
            results = euler_method(f, x0, y0, h, n)
            print_results("Метод Эйлера", results, exact_solution)

        elif choice == '2':
            results = euler_koshi_method(f, x0, y0, h, n)
            print_results("Метод Эйлера-Коши", results, exact_solution)

        elif choice == '3':
            results = runge_kutta_4_method(f, x0, y0, h, n)
            print_results("Метод Рунге-Кутта 4-го порядка", results, exact_solution)

        elif choice == '4':
            print(f"\nПроверка на ОДУ: y' = y - x^2 + 1, y(0) = 0.5, интервал [0, 2]")
            print(f"Шаг h = {h:.4f}, количество шагов n = {n}")

            # Сравним все три метода
            euler_res = euler_method(f, x0, y0, h, n)
            ek_res = euler_koshi_method(f, x0, y0, h, n)
            rk4_res = runge_kutta_4_method(f, x0, y0, h, n)

            print("\n=== Сравнение методов ===")
            print(f"{'x':>8} {'Эйлер':>12} {'Эйлер-Коши':>15} {'РК4':>12} {'Точное':>12}")
            print("-" * 70)
            for i, (x, y_euler) in enumerate(euler_res):
                _, y_ek = ek_res[i]
                _, y_rk4 = rk4_res[i]
                exact_y = exact_solution(x)
                print(f"{x:8.4f} {y_euler:12.6f} {y_ek:15.6f} {y_rk4:12.6f} {exact_y:12.6f}")

        elif choice == '5':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()