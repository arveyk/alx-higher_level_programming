#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum_av = sum_d = 0
    for c, in zip(my_list):
        sum_av += c[0] * c[1]
    for i in my_list:
        sum_d += i[1]
    return sum_av / sum_d
