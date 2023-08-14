#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence == "":
        char = None
    else:
        char = sentence[0]
    tup_le = len(sentence), char
    return tup_le
