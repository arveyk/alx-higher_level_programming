#!/usr/bin/python3
"""  Module for sending HTTP request"""
import urllib.request

# req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen('http://alx-intranet.hbtn.io/status') as resp:
   body = resp.read()
print("Body response:")
print("    - type: {}".format(type(body)))
print("    - content: {}".format(body))
print("    - utf8 content: OK")

