def addition(a, b):
    return a + b


def substruction(a, b):
    return a - b

def main():
    a, operation, b = input().split()
    
    if operation == '+':
        result = addition(float(a), float(b))
    elif operation == '-':
        result = substruction(float(a), float(b))
    elif operation == '*':
        result = multiplication(float(a), float(b))
    elif operation == '/':
        if float(b) == 0:
            print('Деление на 0')
            return
        result = division(float(a), float(b))
    else:
        print('Некорректное выражение')
        return
    
    print(result)
    return