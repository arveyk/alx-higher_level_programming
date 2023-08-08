#!/usr/bin/python3
for r in range(0, 10):
    for s in range(0, r):
        if 10 * (s) + r == s + 10 * (r):
            continue
        print("{:d}{:d}".format(s, r), end="")
        if s < 8:
            print(", ", end="")
print()
