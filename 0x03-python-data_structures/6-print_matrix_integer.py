#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for f in i:
            print("{:d}".format(f), end="")
            if f % len(i) != 0:
                print(" ", end="")
        print()
