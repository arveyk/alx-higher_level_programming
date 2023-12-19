#!/usr/bin/python3
"""  Module for sending HTTP request"""
import urllib.request
#import chardet

req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as resp:
   body = resp.read()

print("Body response:")
print("    - type: {}".format(type(body)))
print("    - content: {}".format(body))
print("    - utf8 content: {}".format(body.decode('utf-8')))
