def main():

    expression = input("Expression: ")

    x, op, z = expression.split()

    x = int(x)
    z = int(z)

    result = None
    if op == '+':
        result = x + z
    elif op == '-':
        result = x - z
    elif op == '*':
        result = x * z
    elif op == '/':
        result = float(x) / z


    print("{:.1f}".format(result))

main()
