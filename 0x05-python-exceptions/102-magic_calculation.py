#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
            if i > a:
                raise Exception('Toofar')
                result = a + b
            else:
                result += (a ** b) / i
    return result
