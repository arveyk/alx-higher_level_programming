#!/usr/bin/python3
def fizzbuzz():
    t = 1
    while t <= 100:
        if t % 15 == 0:
            print("FizzBuzz ", end="")
        elif t % 3 == 0:
            print(f"Fizz ", end="")
        elif t % 5 == 0:
            print(f"Buzz ", end="")
        else:
            print("{:d} ".format(t), end="")
        t += 1
