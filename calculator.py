def main():
    print("введите пример")
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
    else:
        print("такая операция не поддерживается")
        return

    print(res)


# функция сложения
def add(a: float, b: float):
    return a + b


# функция вычитания
def subtract(a: float, b: float):
    return a - b


main()
