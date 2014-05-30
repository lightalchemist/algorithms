#!/usr/bin/env python

"""
File: num_ways_change.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Compute the number of ways to provide change
for an amount "total" given a set of denominations.
"""

import pdb
from functools import update_wrapper
import numpy as np


def decorator(d):
    def _d(fn):
        return update_wrapper(d(fn), fn)

    update_wrapper(_d, d)
    return _d


@decorator
def memo(f):
    cache = {}
    def _f(*args, **kwargs):
        try:
            result = cache[args]
            return result
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            return f(*args)

    return _f


@memo
def num_ways_make_change(n, C, D):
    if n == 0:
        return 0

    if C == 0:
        return 1

    dn = D[n-1]
    if dn > C:
        return num_ways_make_change(n-1, C, D)
    else:
        return (num_ways_make_change(n-1, C, D) +
                num_ways_make_change(n, C-dn, D))


def build_table(D, total):
    nd = len(D)
    A = np.zeros((nd+1, total+1))
    A[:, 0] = 1
    for i in range(1, nd+1):
        for v in range(1, total+1):
            di = D[i-1]
            # pdb.set_trace()
            if di > v:
                A[i][v] = A[i-1][v]
            else:
                A[i][v] = A[i-1][v] + A[i][v - di]

    return A


def main():
    denominations = [1, 2]
    C = 3
    A = build_table(denominations, C)
    num_ways = A[len(denominations), C]
    assert num_ways == 2
    print("Number of ways to change {} using denominations {}:"
          " {}".format(C, denominations, num_ways))
    num_ways = num_ways_make_change(len(denominations),
                                    C,
                                    denominations)
    print(num_ways)


    denominations = [1, 2, 5]
    C = 10
    A = build_table(denominations, C)
    num_ways = A[len(denominations), C]
    assert num_ways == 10
    print("Number of ways to change {} using denominations {}:"
          " {}".format(C, denominations, num_ways))
    num_ways = num_ways_make_change(len(denominations),
                                    C,
                                    denominations)
    print(num_ways)

    denominations = [1, 5, 10, 25, 50]
    C = 11
    A = build_table(denominations, C)
    num_ways = A[len(denominations), C]
    assert num_ways == 4
    print("Number of ways to change {} using denominations {}:"
          " {}".format(C, denominations, num_ways))
    num_ways = A[len(denominations), C]
    num_ways = num_ways_make_change(len(denominations),
                                    C,
                                    denominations)
    print(num_ways)


if __name__ == '__main__':
    main()
