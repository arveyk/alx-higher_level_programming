#!/usr/bin/python3
"""Singly linked list python syle"""


class Node:
    """defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """Initializes args
        Args:
            data: data for new node
            next_node: pointer to next node
        Returns:
            No value
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value
        
    @property
    def next_node(self):
        """
            Getter: retieve the next_node
            Setter: initializes the pointer to next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None or type(value) is not Node:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value

class SinglyLinkedList:
    """Defines a singly linked list"""
    def __init__(self):
        """creates pointer to head node"""
        self.head = None
    def sorted_insert(self, value):
        new_n = Node(value)
        if self.head is None:
            self.head = new_n
        else:
            if self.head.data > value:
                new_n.__next_node = self.head
                self.head = new_n
                return new_n
            trav = self.head
            while trav.next_node:
                if trav.next_node.value > trav.value:
                    new_n.__next_node = trav.next_node
                    trav.next_node = new_n
                    return new_n
                trav = trav.next_node
        self.head = new_n
    def print_l(self):
        if self.head is None:
            return
        n = self.head
        while n is not None:
            print(n.__data)
            n = n.__next_node
