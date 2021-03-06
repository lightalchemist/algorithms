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
    O(1) get size of linked list
"""

from node import Node


class LinkedList(object):

    def __init__(self, items=None):
        self._size = 0
        self._head = None
        if items is not None:
            self._insert_bulk(items)


    def _insert_bulk(self, items):
        for item in items:
            self.insert(item)


    def insert(self, item, pos=None):
        if pos is not None:
            self._check_valid_position(pos, self._size)
        else:  # Default insert at end of linked list
            pos = self._size

        if not isinstance(item, Node):
            item = Node(item)

        self._insert(item, pos)


    def _insert(self, node, pos):
        if self._head is None or pos == 0:
            node.next_element = self._head
            self._head = node
        else:
            head = self._get_node(pos - 1)  # Get node at position before pos
            node.next_element = head.next_element
            head.next_element = node

        self._size += 1


    def _delete_node_at(self, pos):
        self._check_valid_position(pos)
        if pos == 0:
            self._head = self._head.next_element
        else:
            i = 0
            cur_node = self._head
            while i != (pos - 1):
                cur_node = cur_node.next_element
                i += 1

            node = cur_node.next_element
            cur_node.next_element = node.next_element

        self._size -= 1


    def delete_node(self, node):
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

        self._size -= 1


    def _get_node(self, pos):
        self._check_valid_position(pos)
        i = 0
        cur_node = self._head
        while i != pos:
            cur_node = cur_node.next_element
            i += 1

        return cur_node


    def _check_valid_position(self, pos, end=None):
        if end is None:  # Default we can only access item within list.
            end = self._size - 1

        if not (0 <= pos <= end):
            raise ValueError("Given pos: {} not within"
                             " range of linked list.".format(pos))


    @property
    def head(self):
        return self._head


    # @head.setter
    # def head(self, node):
    #     if not isinstance(node, Node):
    #         raise TypeError("Cannot set head of linked list to object that is not a Node.")

    #     if node not in list(self):
    #         self._insert(node, 0)  # This will increment size
    #     else:
    #         raise ValueError("Cannot set other node in current list as head as resulting"
    #                          " list may be ill-defined.")


    def __iter__(self):
        cur_node = self._head
        while cur_node is not None:
            yield cur_node
            cur_node = cur_node.next_element
        raise StopIteration


    def __getitem__(self, pos):
        return self._get_node(pos)


    def __setitem__(self, pos, item):
        self.insert(item, pos)


    def __delitem__(self, pos):
        self._delete_node_at(pos)


    def __len__(self):
        return self._size


    def __str__(self):
        return str([x.value for x in self])


def reverse(linkedlist):
    """Reverse a linked list in O(n) time using O(1) storage."""
    before = None
    current = linkedlist.head
    while current is not None:
        linkedlist._head = current  # Move head to current node
        after = current.next_element
        current.next_element = before  # Reverse pointer
        before = current  # Move pointers 1 step
        current = after

    return before


def test():
    a = LinkedList()
    a.insert(0)
    assert a.head.value == 0
    assert str(a) == "[0]"
    assert a[0].value == 0
    assert len(a) == 1

    a.insert(1)
    assert str(a) == "[0, 1]"
    assert a[0].value == 0
    assert a[1].value == 1
    assert len(a) == 2

    a.insert(-1, 0)
    assert a.head.value == -1
    assert str(a) == "[-1, 0, 1]"

    assert a[0].value == -1
    assert a[1].value == 0
    assert a[2].value == 1
    assert len(a) == 3

    del a[0]
    assert str(a) == "[0, 1]"
    assert a[0].value == 0
    assert len(a) == 2

    node = a[1]
    assert node.value == 1
    a.delete_node(node)
    assert str(a) == "[0]"
    assert len(a) == 1

    a.delete_node(a.head)
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

    a = LinkedList([-1])
    assert str(a) == "[-1]"

    a = LinkedList([1, 2, 3])
    assert str(a) == "[1, 2, 3]"
    assert(len(a)) == 3

    a = LinkedList(set([2, 3]))
    assert str(a) in ["[2, 3]", "[3, 2]"]
    assert(len(a)) == 2

    print("All tests pass.")


if __name__ == '__main__':
    test()
