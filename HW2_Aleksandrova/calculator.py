def multiplication(x, y):
    return x * y
  
def division(x,y):
    return(x / y)
  
def addition(x, y):
    return x + y
  
def subtraction(a, b):
    return a - b
  
def main(x, op, y):
    if op == '+':
        print(addition(float(x),float(y)))
    if op == '*':
        print(multiplication(float(x),float(y)))
    if op == '-':
        print(subtraction(float(x),float(y)))
    if op == '/':
        if y != '0':
            print(division(float(x),float(y)))
        else:
            print('На ноль делить нельзя! Введите другое выражение')

main(*input().split())

