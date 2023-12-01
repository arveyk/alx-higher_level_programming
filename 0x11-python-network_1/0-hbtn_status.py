#!/usr/bin/python3
# Module for sending HTTP request
import urllib.request

#req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen('http://alx-intranet.hbtn.io/status') as resp:
    html = resp.read()

print(html)
