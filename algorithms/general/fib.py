#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: fib.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Standard implementation of computing fibonnaci number.
"""

from functools import update_wrapper


def decorator(d):
    def _d(f):
        return update_wrapper(d(f), f)  # Update decorated f with info from f.

    update_wrapper(_d, d)  # Update wrapped decorator
    return _d


@decorator
def memo(f):
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            value = f(*args)
            cache[args] = value
            return value
        except ValueError:
            return f(*args)

    return _f


@memo
def fib_recurse(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n -1) + fib(n - 2)

def fib(n):
    if n < 0:
        raise ValueError("Negafibonnaci numbers are not supported.")
    elif n == 0:
        return 0

    F1, F2 = 1, 0  # F_{n-1} and F_{n-2}
    for i in range(1, n):
        F1, F2 = F1 + F2, F1

    return F1


def test():
    fib_series = [fib(i) for i in range(10)]  # First 10 fib. numbers including fib(0)
    assert fib_series == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    fib_series = [fib_recurse(i) for i in range(3)]
    assert fib_series == [0, 1, 1]


if __name__ == '__main__':
    test()
