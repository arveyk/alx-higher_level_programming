#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    num2 = number * -1
    print("Last digit of {} is {}".format(number, num2 % 10), end="")
    if num2 % 10 == 0:
        print(" and is 0".format(num2 % 10))
    elif num2 % 10 > 5:
        print(" and is greater than 5")
    if num2 % 10 < 6 and num2 % 10 != 0:
        print(" and is less than 6 and not 0", end="\n")

else:
    print("Last digit of {} is {}".format(number, number % 10), end="")
    if number % 10 == 0:
        print(" and is 0".format(number % 10))
    elif number % 10 > 5:
        print(" and is greater than 5")
    if number % 10 < 6 and number % 10 != 0:
        print(" and is less than 6 and not 0", end="\n")
