#!/us/bin/python3
def no_c(my_string):
    str1 = ""
    for i in my_string:
        if ord(i) == 99 or ord(i) == 67:
            continue
        str1 += i
    return str1
