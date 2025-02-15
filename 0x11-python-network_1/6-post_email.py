#!/usr/bin/python3
''' Script 6, Post email
'''
import requests
import sys


if __name__ == '__main__':
    usremail = {'email': sys.argv[2]}
    url = sys.argv[1]
    ir = requests.post(url, data=usremail)
    print(r.text)
