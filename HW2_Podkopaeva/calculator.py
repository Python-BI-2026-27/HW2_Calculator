def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def main():
    a, operation, b = input().split()
    
    if operation == '+':
        result = addition(float(a), float(b))
    elif operation == '-':
        result = subtraction(float(a), float(b))
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

if __name__ == '__main__':
    main()
