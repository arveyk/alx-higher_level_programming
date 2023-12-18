#!/usr/bin/python3
# Script sends request to url 
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(url) as resp:
        hdr = resp.read()
        print(hdr)
