def subtract(a, b):
    return a - b
def addition(a,b):
    return a+b
def multiply(a, b):
    return a * b
def divide(a,b):
    if b == 0:
        return "Деление на 0!"
    return a/b
def main():
    equation=input('ВВЕДИТЕ: ').split()
    a=float(equation[0])
    b=float(equation[2])
    symbol=equation[1]
    if symbol == "+":
        print(addition(a,b))
    elif symbol == "-":
        print(subtract(a,b))
    elif symbol == "*":
        print(multiply(a,b))
    elif symbol == "/":
        print(divide(a,b))
    else:
        print("Неверно выбрана математическая операция (поддерживается: +,-,*./). Попробуйте снова.")
    
if __name__ == "__main__":
    main()    
