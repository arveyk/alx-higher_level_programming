#!/usr/bin/python3
""" Script that fetches a status from given URL
"""
import requests

url = "https://alx-intranet.hbtn.io/status"
resp = requests.get(url)
print(type(resp.headers["Content-type"]))
print(resp.ok)
