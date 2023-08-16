#!/usr/bin/python3


def best_score(a_dictionary):
    e = 0
    if a_dictionary is None:
        return None
    for key in a_dictionary:
        if a_dictionary[key] is None:
            return None
        else:
            if a_dictionary[key] > e:
                e = a_dictionary[key]
    for key in a_dictionary:
        if a_dictionary is None:
            pass
        else:
            if e == a_dictionary[key]:
                return key
