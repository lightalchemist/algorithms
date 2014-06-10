#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: linked_list.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Basic implementation of linked list.
Supports:
    O(n) insertion, deletion
    O(n) retrieval of node at given position
    O(1) get length of linked list
"""

class Node(object):
    def __init__(self, value, next_element=None):
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


class LinkedList(object):

    def __init__(self):
        self._length = 0
        self._head = None


    def insert(self, n, pos=None):
        if pos is not None:
            self._check_valid_position(pos, self._length)
        else:  # Default insert at end of linked list
            pos = self._length

        if not isinstance(n, Node):
            n = Node(n)

        self._insert(n, pos)


    def _insert(self, node, pos):
        if self._head is None or pos == 0:
            node.next_element = self._head
            self._head = node
        else:
            head = self.get_node(pos - 1)  # Get node at position before pos
            node.next_element = head.next_element
            head.next_element = node

        self._length += 1


    def delete(self, node):
        cur_node = self._head
        if node == self._head:
            self._head = self._head.next_element
        else:
            while cur_node is not None and cur_node.next_element != node:
                cur_node = cur_node.next_element

            if cur_node is None:
                raise ValueError("Unable to delete node {}"
                                 " as it is not in linked list.".format(node))

            # Disconnect node from its parent and connect it's children to it.
            cur_node.next_element = node.next_element

        self._length -= 1
        assert self._length >= 0


    def get_node(self, pos):
        self._check_valid_position(pos)
        i = 0
        cur_node = self.head
        while i != pos:
            cur_node = cur_node.next_element
            i += 1

        return cur_node


    def _check_valid_position(self, pos, end=None):
        if end is None:  # Default we can only access item within list.
            end = self._length - 1

        if not (0 <= pos <= end):
            raise ValueError("Given pos: {} not within"
                             "range of linked list.".format(pos))


    @property
    def head(self):
        return self._head


    def __iter__(self):
        cur_node = self._head
        while cur_node is not None:
            yield cur_node
            cur_node = cur_node.next_element
        raise StopIteration


    def __len__(self):
        return self._length


    def __str__(self):
        return str([x.value for x in self])


def test():
    a = LinkedList()
    a.insert(0)
    assert a.head.value == 0
    assert str(a) == "[0]"
    assert a.get_node(0).value == 0
    assert len(a) == 1

    a.insert(1)
    assert str(a) == "[0, 1]"
    assert a.get_node(0).value == 0
    assert a.get_node(1).value == 1
    assert len(a) == 2

    a.insert(-1, 0)
    assert a.head.value == -1
    assert str(a) == "[-1, 0, 1]"
    assert a.get_node(0).value == -1
    assert a.get_node(1).value == 0
    assert a.get_node(2).value == 1
    assert len(a) == 3

    a.delete(a.head)
    assert str(a) == "[0, 1]"
    assert a.get_node(0).value == 0
    assert len(a) == 2

    node = a.get_node(1)
    assert node.value == 1
    a.delete(node)
    assert str(a) == "[0]"
    assert len(a) == 1

    a.delete(a.head)
    assert a.head == None
    assert len(a) == 0

    node = Node(1)
    a.insert(node)
    assert str(a) == "[1]"
    assert len(a) == 1
    assert a.head == node

    node = Node(2)
    a.insert(node, 1)
    assert str(a) == "[1, 2]"

    a.insert(3, 2)
    assert str(a) == "[1, 2, 3]"
    assert len(a) == 3


if __name__ == '__main__':
    test()
