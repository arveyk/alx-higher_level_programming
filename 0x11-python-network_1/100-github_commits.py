#!/usr/bin/python3
''' Script to retieve github commits
based on the user name and repo name
'''
import requests
import sys

if __name__ == '__main__':
    '''Where the action is. The above statement ensures that
    the script is not run when imported
    Args:
        from the command line
        first : repo name
        second: user name
    '''
    repo = sys.argv[1]
    name = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        name, repo)
    resp = requests.get(url)
    Json_R = resp.json()
    repo_len = len(Json_R)
    for i in range(repo_len):
        print('{}: {}'.format(Json_R[i].get('sha'),
                              Json_R[i]['commit']['author']['name']))
