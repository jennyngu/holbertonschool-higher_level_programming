#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    arg = sys.argv
    if len(arg) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = arg[2]
    if op not in '+-*/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    num_1 = int(arg[1])
    num_2 = int(arg[3])
    if op == '+':
        result = add(num_1, num_2)
    elif op == '-':
        result = sub(num_1, num_2)
    elif op == '*':
        result = mul(num_1, num_2)
    elif op == '/':
        result = div(num_1, num_2)
    print("{} {} {} = {}".format(num_1, op, num_2, result))
