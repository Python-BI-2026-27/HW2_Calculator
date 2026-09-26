def main():
    num1, op, num2 = input("Введите выражение:\n").split()
    num1, num2 = float(num1), float(num2)
    
    if op == "+":
        result = add(num1, num2)
    elif op == "-":
        result = subtract(num1, num2)
    elif op == "*":
        result = multiply(num1, num2)
    elif op == "/":
        if num2 == 0:
            result = "Ошибка: деление на 0"
        else:
            result = divide(num1, num2)
    print(result)
  
def subtract(a, b):
    return a - b
  
def multiply(a, b):
    return a * b
  
def add(a, b):
    return a + b

def divide(a, b):
    return a / b

   



main()

