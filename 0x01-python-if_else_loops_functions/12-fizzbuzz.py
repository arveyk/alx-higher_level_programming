#!/usr/bin/python3


def fizzbuzz():
    for i in range(1, 101, 1):
        if i % 15 == 0:
            print("Fizzbuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        print("{} ".format(i))
