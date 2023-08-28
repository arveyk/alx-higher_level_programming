#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    l1 = len(my_list_1)
    l2 = len(my_list_2)
    for i in range(list_length):
        try:
            new_list.append(my_list_1[i] / my_list_2[i])
        except IndexError:
            new_list.append(0)
            print("out of range")
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        except TypeError:
            new_list.append(0)
            print("wrong type")
    return new_list
