#!/usr/bin/python3
""" Script to read and parse from stdin"""
import sys

count = 0;
try:
    report = sys.stdin
    for line in report:
        if (count % 10):
            print('File size:{}'.format(line[-4:-2]))
        print(': {}'.format(line[-2:]))
        count += 1
except KeyboardInterrupt:
    print('File size:{} {}'.format(line[0:5], len(line)))
