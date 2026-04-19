# Дмитрий Ткаченко

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


def multiply(a, b):
    return a*b

def sqrt(x):
    if x<0:
        raise ValueError("Попытка извлечения корня из отрицательного числа")
    return math.sqrt(x)

if __name__ == "__main__":
    print("Простой калькулятор запущен.")
    print(f"2 + 2 = {add(2, 2)}")
