# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, value=None, next_element=None):
        self._next_element = next_element
        self._value = value

    @property
    def next_element(self):
        return self._next_element

    @next_element.setter
    def next_element(self, element):
        self._next_element = element

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    def __str__(self):
        return "Node with value {}".format(self.value)
