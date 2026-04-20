# Автор: Aleksandr Lisenkov

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    # TODO: не реализовано
    return a * b

def sqrt(x):
    import math
    return math.sqrt(x)


if __name__ == "__main__":
    print("Простой калькулятор запущен.")
    print(f"2 + 2 = {add(2, 2)}")
    print(f"Квадратный корень из x равен: {sqrt(25)}")

