#!/usr/bin/python3
# Script sends request to url 
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as req:
        resp = req.read()
        
    for strg in resp:
        if strg == "X-Request-Id":
            print(strg)
