#!/usr/bin/python3
def lazy_matrix_mul(m_a, m_b):
    import numpy as np
    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')
    try:
        mult = np.dot(m_a, m_b)
    except Exception as e:
        print(e)
    return mult

