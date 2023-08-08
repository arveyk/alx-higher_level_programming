#!/usr/bin/python3
def remove_char_at(str, n):
    ch = ""
    len_str = 0
    for l in str:
        if len_str == n:
            pass
        else:
            ch += l
        len_str += 1
    return ch
