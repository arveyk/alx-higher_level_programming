#!/usr/bin/python3
def print_last_number(number):
    if number < 0:
        number *= -1
    print(number % 10)
