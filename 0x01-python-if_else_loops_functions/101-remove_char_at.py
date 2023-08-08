#!/usr/bin/python3
def remove_char_at(str, n):
    ch = ""
    len_str = 0
    for search in str:
        if len_str == n:
            pass
        else:
            ch += search
        len_str += 1
    return ch
