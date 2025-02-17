#!/usr/bin/python3
'''Ger response header
'''
import requests
import sys


if __name__ == '__main__':
    '''
    Script to get json response from an api and search name and id
    '''
    url = 'https://api.github.com/users/{}'.format(sys.argv[1])
    headers = {'Accept': 'Application/vnd.github+json',
               'Authorization': 'Bearer {}'.format(sys.argv[2]),
               'X-GitHub-Api-Version': '2022-11-28'
               }
    r = requests.get(url, headers=headers)
    res_Json = r.json()
    if res_Json is None:
        print('None')
    else:
        print('{}'.format(res_Json.get('id')))
