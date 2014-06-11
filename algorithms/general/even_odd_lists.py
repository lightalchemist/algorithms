#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: even_odd_lists.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Rearrange a linked list so that nodes at even positions
appear before those at odd positions.

Constraints: Use O(n) time and O(1) additional storage.

Problem 7.6 Pg 64 of Elements of Programming Interview
"""

if __name__ == '__main__':
    import sys
    sys.path.insert(0, "..")


from data_structures.linked_list import LinkedList


def rearrange_even_odd(linkedlist):
    h0 = linkedlist.head
    if h0 is None:  # Empty linked list
        return

    h1 = h0.next_element
    t0 = h0
    while True:
        # Move t1
        t1 = t0.next_element
        if t1 is None:  # Last element even
            break
        else:
            # Set t0 next
            t0.next_element = t1.next_element

        if t1.next_element is None:  # Last element odd
            # t0 next element already set to None
            break
        else:
            # Move t0
            t0 = t1.next_element
            # Set t1 next
            t1.next_element = t0.next_element

    t0.next_element = h1  # Connect list of odd nodes to tail of even nodes.


def test():
    a = LinkedList(range(1))
    rearrange_even_odd(a)
    assert str(a) == "[0]"
    assert len(a) == 1

    a = LinkedList(range(2))
    rearrange_even_odd(a)
    assert str(a) == "[0, 1]"
    assert len(a) == 2

    a = LinkedList(range(3))
    rearrange_even_odd(a)
    assert str(a) == "[0, 2, 1]"
    assert len(a) == 3

    a = LinkedList(range(4))
    rearrange_even_odd(a)
    assert str(a) == "[0, 2, 1, 3]"
    assert len(a) == 4

    a = LinkedList(range(5))
    rearrange_even_odd(a)
    assert str(a) == "[0, 2, 4, 1, 3]"
    assert len(a) == 5

    a = LinkedList(range(6))
    rearrange_even_odd(a)
    assert str(a) == "[0, 2, 4, 1, 3, 5]"
    assert len(a) == 6

    a = LinkedList()
    rearrange_even_odd(a)
    assert str(a) == "[]"
    assert len(a) == 0

    print("All tests pass.")


if __name__ == '__main__':
    test()
