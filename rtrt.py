import math

def f(x):
    return x * math.sin(x) - 1

def bisection(a, b, eps=1e-4):
    if f(a) * f(b) >= 0:
        print("Корня на отрезке нет")
        return None
    print(f"{'Итер':<5} {'a':<10} {'b':<10} {'c':<10} {'f(c)':<12}")
    iter_count = 0
    while (b - a) > eps:
        c = (a + b) / 2
        fc = f(c)
        iter_count += 1
        print(f"{iter_count:<5} {a:<10.6f} {b:<10.6f} {c:<10.6f} {fc:<12.6f}")
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

root = bisection(1.0, 2.0, 1e-4)
print(f"\nКорень ≈ {root:.6f}")