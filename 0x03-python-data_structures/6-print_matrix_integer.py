#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        z = 0
        for f in i:
            print("{:d}".format(f), end="")
            z += 1
            if z % len(i) != 0:
                print(" ", end="")
        print()
