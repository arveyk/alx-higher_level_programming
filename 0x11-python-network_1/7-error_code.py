#!/usr/bin/python3
'''Ger response header
'''
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-id'))
    if r.status_code > 399:
        print('Error code: {}'.format(r.status_code))
    else:
        print(r.text)
