#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
File: rotate_array.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Rotate an array in place.
"""


def rotate2(array, head, size):
    size = len(array)
    buffer = array[:head]
    # Need to move len(array) - len(buffer) items
    for i in range(size - len(buffer)):
        array[i] = array[(head + i) % size]

    for j, i in enumerate(range(size - len(buffer), size)):
        array[i] = buffer[j]


def rotate(array, first, middle, last):
    """Rotate subarray array[first:last] in place so that
    the element array[middle] gets rotated circularly to position "first"
    This implementation is a port of the rotate function in C++.
    E.g.,
    array = [0, 1, 2, 3]
    rotate(array, 1, 2, 3); array -> [0, 2, 1, 3]
    """


    assert first <= middle < last

    i = 0
    n = middle
    while first != n:
        array[first], array[n] = array[n], array[first]
        first += 1
        n += 1
        if n == last:
            n = middle
        elif first == middle:
            middle = n
        i += 1


def test():
    array = range(5)
    rotate2(array, 0, len(array))

    array = [0, 1, 2, 3]
    rotate(array, 1, 2, 3)
    assert array == [0, 2, 1, 3]


if __name__ == '__main__':
    test()
