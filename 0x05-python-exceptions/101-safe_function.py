#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
    except Exception as qw:
        print("Exception: {}".format(qw), file=sys.stderr)
        return None
    return result
