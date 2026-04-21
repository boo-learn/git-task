# Автор: Василий Никитин


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def sqrt(x):
    if x < 0:
        raise ValueError("Нельзя извлечь корень из отрицательного числа")
    return int(math.sqrt(x))


import math
if __name__ == "__main__":
    print("Простой калькулятор запущен.")
    print(f"5 + 2 = {add(5, 2)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"5 * 2 = {multiply(5, 2)}")
    print(f"Кореень из 9 = {sqrt(9)}")