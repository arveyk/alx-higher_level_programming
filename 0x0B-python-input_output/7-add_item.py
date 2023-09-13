#!/usr/bin/python3
"""Module to add all args to a Python list and save to file
"""

import json
import sys

args_len = len(sys.argv)
save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file

save_list = []

while s < args_len:
    save_list.append(sys.argv[s])

with open(0, encoding='utf-8') as cmd_line:
    for i in cmd_line:
        save_list.append(i)

with open('add_item.json', mode="w", encoding='utf-8') as add_item:
    json.dump(save_list, add_item)
