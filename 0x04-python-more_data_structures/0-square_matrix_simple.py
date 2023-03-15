#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_mat = list(map(lambda x: x ** 2, list(matrix)))
    return new_mat
