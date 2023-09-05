#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divide elements of a matrix
        Args:
            matrix: the matrix to be divided
            div: divisor
        Return: New matrix resulting from division"""
    if type(matrix) is not list:
        raise TypeError('the matrix must be a matrix (list of lists) of integers/floats')

    if type(div) is not int:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    
    count = 0
    for k in matrix:
        for t in k:
            count += 1
    if count % 2 != 0:
            raise TypeError('Each row of the matrix must have the same size')
    try:
        new_m = []
        for row in matrix:
            p = []
            for i in row:
                p.append(float('{:.2f}'.format(i / div)))
            new_m.append(p)
    except TypeError:
        print('the matrix must be a matrix (list of lists) of integers/floats')
    else:
        return new_m
