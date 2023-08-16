#!/usr/bin/python3
def roman_to_int(roman_string):
    y = 0
    if roman_string == "MMM":
        return 3000
    s = len(roman_string)
    for i in range(s):
        if roman_string[i] == 'M':
            y += 1000
        if roman_string[i] == 'C':
            if i < s - 2 and roman_string[i + 1] == 'M':
                y += 900
            else:
                y += 100
        if roman_string[i] == 'I':
            if i < s - 2 and roman_string[i + 1] == 'X':
                y += 9
            else:
                y += 1
        if roman_string[i] == 'V':
            y += 5
        if roman_string[i] == 'X':
            y += 10
    return y
