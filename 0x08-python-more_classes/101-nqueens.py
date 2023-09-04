#!/usr/bin/python3
"""Attempts to solve N queens puzzle"""

import sys

d = int(sys.argv[1])
if type(d) is not int:
    print('N must be a number')
    exit(1)
if d < 4:
    print('N must be at least 4')
    exit(1)

mat = []
for i in range(d):
    z = []
    for j in range(d):
        if i == j:
            continue
        z.append(j)
    mat.append(z)

print(mat)
