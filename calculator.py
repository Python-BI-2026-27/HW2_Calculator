import random

WORDS = [
    "потрясающий",
    "невероятный",
    "оригинальный",
    "чудесный",
    "великолепный",
    "восхитительный",
    "блестящий",
    "изумительный",
    "фантастический",
    "превосходный",
    "животрепещущий",
]


def main():
    print(f"Введите Ваш {random.choice(WORDS)} пример:")
    p = input().split()
    # p[1] - возможные операции с числами, p[0] и p[2] - числа
    if len(p) != 3:
        print("это посчитать не получится")
        return
    else:
        a = float(p[0])
        b = float(p[2])
        o = p[1]

    # выбор операции
    if o == "-":
        res = subtract(a, b)
    elif o == "+":
        res = add(a, b)
    elif o == "*":
        res = multiply(a, b)
    elif o == "/":
        res = divide(a, b)
    else:
        print("такая операция не поддерживается")
        return
    print(f"Вот Ваш {random.choice(WORDS)} ответ:")
    print("( •_•)O*¯`·.", res, ".·´¯`°Q(•_• )")


# функция сложения
def add(a: float, b: float):
    return a + b


# функция вычитания
def subtract(a: float, b: float):
    return a - b


# функция умножения
def multiply(a: float, b: float):
    return a * b


# функция деления
def divide(a: float, b: float):
    if b == 0:
        return "Деление на 0 невозможно"
    else:
        return a / b


main()
