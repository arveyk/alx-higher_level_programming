#!/usr/bin/python3
''' Script to list github commits
'''
import requests
import sys

repo = sys.argv[1]
name = sys.argv[2]

url = 'https://api.github.com/repos/{}/{}/commits'.format(
        name, repo)
resp = requests.get(url)
Json_R = resp.json()

for i in range(10):
    print('{}: {}'.format(Json_R[i].get('sha'),
                          Json_R[i]['commit']['author']['name']))
