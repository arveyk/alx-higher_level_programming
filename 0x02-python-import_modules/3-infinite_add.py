#!/usr/bin/python3
import sys
n = len(sys.argv)
summ = 0
for i in range(n):
    summ += int(sys.argv[i])
    if i == 0:
        summ += 0
        print("{}".format(summ))
    print("{}".format(summ))
