#!/usr/bin/python3
'''Ger response header
'''
import requests
import sys


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) < 2:
        r = requests.post(url, data={'q': ''})
    else:
        r = requests.post(url, data={'q': sys.argv[1]})
        if len(r.text) > 0:
            if not validJson:
                print('Not a valid JSON')
            Json_R = None
            Json_R = r.json()
            if Json_R:
                print('No result')
            else:
                print('[{}] {}'.format(Json_R.get('id', Json_R.get('name')))
