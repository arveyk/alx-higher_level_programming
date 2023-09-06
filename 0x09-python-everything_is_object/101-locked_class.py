#!/usr/bin/python3
class LockedClass(object):

    __slots__ = ['first_name']

    def __init__(self, first=None):
        self.first_name = first
