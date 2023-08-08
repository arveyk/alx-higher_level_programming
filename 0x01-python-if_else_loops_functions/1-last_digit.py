#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    rem = -number % 10
    rem *= -1
else:
    rem = number % 10
print(f"Last digit of {number:d} is {rem:d} ", end="")
if rem > 5:
    print(f"and is greater than 5")
elif rem == 0:
    print(f"and is 0")
elif rem < 6 and rem != 0:
    print("and is less than 6 and not 0")
