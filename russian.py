#!/usr/bin/env python

"""
File: russian.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Implementation of Russian Peasant multiplication algorithm.
"""

def russian(x, y):
    z = 0
    while x > 0:
        if x % 2:
            z += y

        x = x >> 1
        y = y << 1

    return z


def recursive_russian(a, b):
    if a == 0:
        return 0

    if a % 2 == 0:
        return 2 * recursive_russian(a // 2, b)
    else:
        return b + 2 * recursive_russian((a - 1)//2, b)


def test():
    assert russian(1, 1) == 1
    assert russian(1, 0) == 0
    assert russian(0, 0) == 0
    assert russian(2, 1) == 2
    assert russian(2, 3) == 6
    assert russian(3, 3) == 9
    assert russian(3, 7) == 21
    assert russian(11, 159) == 11 * 159

    assert recursive_russian(1, 1) == 1
    assert recursive_russian(1, 0) == 0
    assert recursive_russian(0, 0) == 0
    assert recursive_russian(2, 1) == 2
    assert recursive_russian(2, 3) == 6
    assert recursive_russian(3, 3) == 9
    assert recursive_russian(3, 7) == 21
    assert recursive_russian(11, 159) == 11 * 159


if __name__ == '__main__':
    test()
