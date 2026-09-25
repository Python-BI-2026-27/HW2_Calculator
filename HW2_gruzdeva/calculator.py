def subtraction(x, y):
    return x - y


def main():
    # Ввод строки с математическим выражением, числа разделены пробелами
    user_input = input("Введите выражение:")

    # Разбиваем выражение по пробелам на числа
    elements = user_input.split()

    # Переводим 1 и 3 элементы в числа
    num1 = float(elements[0])
    num2 = float(elements[2])
    operator = elements[1]

    # Проверка на математическую операцию
    if operator == "+":
        output = add(num1, num2)
    elif operator == "-":
        output = subtraction(num1, num2)
    elif operator == "*":
        output = multiply(num1, num2)
    elif operator == "/":
        output = divide(num1, num2)
    else:
        print("Операция неизвестна данному калькулятору")
        return

    # Итоговый результат
    print(output)


# Функции членов команды №7 (add, subtraction, multiply, divide)

def add(num1, num2):
    return num1 + num2

def divide(num1, num2):
    result = num1 / num2
    return result

def multiply(num1, num2):
    return num1 * num2


if __name__ == "__main__":
    main()
