def main_func(a, b, op):
    if op == '+':
        add(a,b)
    elif op == '-':
        subtract(a,b)
    elif op == '*' or op == 'x':
        mul(a,b)
    elif op == '/' or op == ':':
        divide(a,b)
    else:
        print('Математическая операция не распознана. Пожалуйста, введите другое выражение!')

a, op, b = input("Введите выражение:").split(sep = ' ')
a = float(a)
b = float(b)
main_func(a, b, op)
