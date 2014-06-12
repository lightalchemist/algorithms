#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: sunset.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Solution to problem 8.6 pg 69 of Elements of Programming Interview book.
"""

from stack import Stack

def solve(heights):
    """heights is an iterable containing the heights
    of the buildings ordered from east to west."""
    s = Stack()
    for h in heights:
        while not s.empty() and h > s.top():
            s.pop() # Keep popping if newly encountered building is taller than those before it.

        s.push(h)  # Add in this new building

    return s


def test():
    heights = [10, 7, 3, 9, 5]
    s = solve(heights)
    assert str(s) == "[5, 9, 10]"

    heights = [10, 7, 3]
    s = solve(heights)
    assert str(s) == "[3, 7, 10]"

    heights = [10, 7, 3, 11]
    s = solve(heights)
    assert str(s) == "[11]"

    heights = [5, 10, 7, 3, 6]
    s = solve(heights)
    assert str(s) == "[6, 7, 10]"


if __name__ == '__main__':
    test()
