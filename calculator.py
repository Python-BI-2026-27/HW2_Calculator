def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b


def summa(a, b):
    return a + b


def multiply(a, b):
    return a * b

def minus(a, b):
    return a - b

def main():
    user_input = input()

    a, symbol, b = user_input.split()
    
    a = float(a)
    b = float(b)

    if symbol == "/":
        result = divide(a, b)
    elif symbol  == "+":
        result = summa(a, b)
    elif symbol == "*":
        result = multiply(a, b)
    elif symbol == "-":
        result = minus(a, b)

    print(result)
main()