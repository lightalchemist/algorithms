#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: stack.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Implementation of standard stack using a linked list.
In addition, supports finding max element in O(1) time.

This implementation is merely for self-study and is
not necessarily a practical one.
In particular, this implementation is not thread-safe.
"""


from linked_list import LinkedList


class Stack(LinkedList):

    def __init__(self, items=None):
        super(Stack, self).__init__()
        if items is not None:
            self._insert_bulk(items)


    def _insert_bulk(self, items):
        current_max = -float("inf")  # Negative infinity
        for i in items:
            current_max = max(current_max, i)
            self.insert((i, current_max), 0)


    def top(self):
        if self.empty():
            raise IndexError("Cannot look at top of empty stack.")

        return self._head.value[0]


    def pop(self):
        item, max_val = self[0].value
        del self[0]
        return item


    def push(self, item):
        if self.empty():
            self.insert((item, item), 0)
        else:
            max_val = max(item, self.head.value[1])
            self.insert((item, max_val), 0)


    def max(self):
        return self._head.value[1]


    def empty(self):
        return self._head is None


    def __str__(self):
        items = [node.value[0] for node in self]
        return str(list(items))


def test():
    s = Stack()
    assert s.empty()
    assert len(s) == 0


    s = Stack([1, 2, 3, 4])
    assert s.top() == 4
    assert s.max() == 4

    assert s.pop() == 4
    assert s.max() == 3
    s.push(1)
    assert s.max() == 3
    assert len(s) == 4
    assert s.pop() == 1
    assert not s.empty()

    s = Stack([1])
    assert not s.empty()
    assert s.top() == 1
    assert s.pop() == 1
    assert len(s) == 0
    assert s.empty()

    print("All tests pass.")


if __name__ == '__main__':
    test()
