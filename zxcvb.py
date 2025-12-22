import math


def runge_kutta_4_system(f1, f2, x0, y1_0, y2_0, h, n):
    """
    Решение системы двух ОДУ методом Рунге-Кутта 4-го порядка.

    Параметры:
        f1, f2 — функции правых частей: dy1/dx = f1(x, y1, y2), dy2/dx = f2(x, y1, y2)
        x0, y1_0, y2_0 — начальные условия
        h — шаг
        n — количество шагов

    Возвращает список кортежей (x, y1, y2)
    """
    x = x0
    y1 = y1_0
    y2 = y2_0
    results = [(x, y1, y2)]

    for i in range(n):
        # Вычисление коэффициентов k1, k2, k3, k4 для y1 и y2
        k1_y1 = h * f1(x, y1, y2)
        k1_y2 = h * f2(x, y1, y2)

        k2_y1 = h * f1(x + h / 2, y1 + k1_y1 / 2, y2 + k1_y2 / 2)
        k2_y2 = h * f2(x + h / 2, y1 + k1_y1 / 2, y2 + k1_y2 / 2)

        k3_y1 = h * f1(x + h / 2, y1 + k2_y1 / 2, y2 + k2_y2 / 2)
        k3_y2 = h * f2(x + h / 2, y1 + k2_y1 / 2, y2 + k2_y2 / 2)

        k4_y1 = h * f1(x + h, y1 + k3_y1, y2 + k3_y2)
        k4_y2 = h * f2(x + h, y1 + k3_y1, y2 + k3_y2)

        # Обновление значений
        y1 = y1 + (k1_y1 + 2 * k2_y1 + 2 * k3_y1 + k4_y1) / 6
        y2 = y2 + (k1_y2 + 2 * k2_y2 + 2 * k3_y2 + k4_y2) / 6
        x = x + h

        results.append((x, y1, y2))

    return results


def print_results(results):
    """Вывод результатов в виде таблицы"""
    print(f"{'x':>8} {'y1':>12} {'y2':>12}")
    print("-" * 35)
    for x, y1, y2 in results:
        print(f"{x:8.4f} {y1:12.6f} {y2:12.6f}")


def main():
    print("=== Решение системы двух ОДУ методом Рунге-Кутта 4-го порядка ===")

    while True:
        print("\nВыберите действие:")
        print("1. Ввести свои функции и начальные условия")
        print("2. Пример: система dy1/dx = y2, dy2/dx = -y1 (гармонический осциллятор)")
        print("3. Пример: система dy1/dx = y1 + y2, dy2/dx = y1 - y2")
        print("4. Выход")

        choice = input("Введите номер: ").strip()

        if choice == '4':
            print("Выход из программы.")
            break

        # Начальные условия по умолчанию
        x0 = 0.0
        y1_0 = 1.0
        y2_0 = 0.0
        h = 0.1
        n = 20

        if choice == '1':
            print("\nВведите функции f1(x, y1, y2) и f2(x, y1, y2) в виде Python-выражений.")
            print("Пример: y2, -y1")
            try:
                f1_str = input("f1(x, y1, y2) = ").strip()
                f2_str = input("f2(x, y1, y2) = ").strip()

                # Создаем лямбда-функции
                f1 = lambda x, y1, y2: eval(f1_str, {"x": x, "y1": y1, "y2": y2, "math": math})
                f2 = lambda x, y1, y2: eval(f2_str, {"x": x, "y1": y1, "y2": y2, "math": math})

                x0 = float(input("Начальное значение x0: "))
                y1_0 = float(input("Начальное значение y1(0): "))
                y2_0 = float(input("Начальное значение y2(0): "))
                h = float(input("Шаг h: "))
                n = int(input("Количество шагов n: "))

            except Exception as e:
                print(f"Ошибка ввода или вычисления: {e}")
                continue

        elif choice == '2':
            print("\nПример: гармонический осциллятор")
            print("dy1/dx = y2")
            print("dy2/dx = -y1")
            f1 = lambda x, y1, y2: y2
            f2 = lambda x, y1, y2: -y1

        elif choice == '3':
            print("\nПример: dy1/dx = y1 + y2, dy2/dx = y1 - y2")
            f1 = lambda x, y1, y2: y1 + y2
            f2 = lambda x, y1, y2: y1 - y2

        else:
            print("Неверный выбор. Попробуйте снова.")
            continue

        # Решаем систему
        try:
            results = runge_kutta_4_system(f1, f2, x0, y1_0, y2_0, h, n)
            print(f"\nРезультаты (шаг h = {h}, n = {n}):")
            print_results(results)
        except Exception as e:
            print(f"Ошибка при решении: {e}")


if __name__ == "__main__":
    main()