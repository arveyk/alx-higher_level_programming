#!/usr/bin/python3


for i in range(10):
    for p in range(9):
        if i == p or i*10 + p == 10*p + i:
            continue
        print("{}{}".format(i, p), end="")
        if i < 9 or p < 9:
            print(",", end=" ")
print()
