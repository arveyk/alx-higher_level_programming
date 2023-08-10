#!/usr/bin/python3
if __name__=="__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    argc = len(argv)
    res = 0
    #signs = '+-*/'
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])

    if argv[2] == '+':
        res = a + b
        print("{:d} + {:d} = {:d}".format(a ,b, res))
    elif argv[2] == '-':
        res = a + b
        print("{:d} - {:d} = {:d}".format(a ,b, res))
    elif argv[2] == '*':
        res = a * b
        print("{:d} * {:d} = {:d}".format(a ,b, res))
    elif argv[2] == '/':
        res = a / b
        print("{:d} / {:d} = {:d}".format(a ,b, res))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


