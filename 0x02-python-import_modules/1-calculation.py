#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

print("{} + {} = {:d}".format(a, b, add(a, b)))
print("{} - {} = {:d}".format(a, b, sub(a, b)))
print("{} * {} = {:d}".format(a, b, mul(a, b)))
print("{} / {} = {:.0f}".format(a, b, div(a, b)))
