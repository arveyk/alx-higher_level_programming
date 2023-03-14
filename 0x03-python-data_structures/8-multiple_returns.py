#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        b = None
    else:
        b = sentence[0]
    tup = (len(sentence), b)
    return tup
