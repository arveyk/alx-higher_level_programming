#!/usr/bin/python3
"""Module to add all args to a Python list and save to file
"""

import json
import sys

args_len = len(sys.argv)
save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file

save_list = []
s = 1
if args_len > 1:
    while s < args_len:
        save_list.append(sys.argv[s])
        s += 1
save_to_json(save_list, 'add_item.json')
