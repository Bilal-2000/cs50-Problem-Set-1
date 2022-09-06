def main():
    expr = input("Expression: ").split(" ")
    print(Math_interpreter(expr))


def Math_interpreter(expr):
    x = int(expr[0])
    y = expr[1]
    z = int(expr[2])
    if y == "+":
        return float(x + z)
    elif y == "-":
        return float(x - z)
    elif y == "*":
        return float(x * z)

    elif y == "/":
        if z == 0:
            try:
                result = z / 0
            except ZeroDivisionError:
                print("Dividing by zero is not allowed")
        else:
            return float(x / z)

    else:
        print("Wrong input")


main()
