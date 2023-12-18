#!/usr/bin/python3
""" Mudule to send request
"""
import urllib.request
import sys

if __name__ == '__main__':
    """ Fails to execute when imported on account
    of the above if statement
    """
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.Request(url) as req:
        try:
            urllib.request.urlopen(req) as resp:
        except urllib.error.HTTPError as err:
            print("Error code: ", err.code)
