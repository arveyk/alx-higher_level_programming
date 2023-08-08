#!/usr/bin/python3
for q in range(97, 123):
    if q == 101 or q == 113:
        continue
    print("{}".format(chr(q)), end="")
