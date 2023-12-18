#!/usr/bin/python3
""" Module to send a request and display the value of X-Request-Id
"""
import urllib.request
import urllib.parse as parse
import sys


if __name__ == "__main__":
    """ Only functions when not imported
    """
    url = sys.argv[1]
    data_dict = {"email" : sys.argv[2]}
    data = parse.urlencode(data_dict)
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as resp:
        page = resp.read().decode('utf-8')
        print(page)
