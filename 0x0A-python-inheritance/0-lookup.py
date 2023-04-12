#!/usr/bin/python3
""" lookup: function that returns list of \
        available atttibutes"""


def lookup(obj):
    return list(dir(obj))
