#!/usr/bin/python3
raise_exception = __import__('5-raise_exception').raise_exception

try:
    raise_exception()
exception TypeError as te:
    print("Exception raised")
