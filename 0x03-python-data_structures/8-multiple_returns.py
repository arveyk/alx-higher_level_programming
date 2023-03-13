#!/usr/bin/python3
def multiple_returns(sentence):
    b = sentence[0]
    if len(sentence) == 0:
        b = None
    tup = (len(sentence), b)
    return tup
