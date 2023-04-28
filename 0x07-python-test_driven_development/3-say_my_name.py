#!/usr/bin/python3
""" Function that prints out name passed to it """

def say_my_name(first_name, last_name=""):
    try:
        print("My name is {:s} {:s}".format(first_name, last_name))
    except Exception as e:
        print("{}  must be a string".format(e))

