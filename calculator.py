def multiply(a, b):
    return a * b


def main():
    input_string = input().split()

    # Преобразуем ввод float или int
    in_a, op, in_b = input_string
    a = float(in_a) if "." in in_a else int(in_a)
    b = float(in_b) if "." in in_b else int(in_b)

    #Заготовка для функций, вставьте свое название.
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    if op in operations:
        result = operations[op](a, b)
        print(result)


if __name__ == "__main__":
    main()
