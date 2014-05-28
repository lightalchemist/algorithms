#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: brick_wall.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist

Description:
http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=11&page=show_problem&problem=841

If we want to build a brick wall out of the usual size of
brick which has a length twice as long as its height
(i.e., length = 2 unit, height = 1 unit),
and if our wall is to be two units tall,
we can make our wall in a number of patterns,
depending on how long we want it. From the figure one observe that:

        _
 1 |   | |
   |___|_|_______________________

        _  _      ____
 2 |   | || |    |____|
   |___|_||_|____|____|__________

        _  _  _      _ ____      ____ _
 3 |   | || || |    | |____|    |____| |
   |___|_||_||_|____|_|____|____|____|_|

There is just one wall pattern which is 1 unit wide -
made by putting the brick on its end.

There are 2 patterns for a wall of length 2:
    two side-ways bricks laid on top of each other and
    two bricks long-ways up put next to each other.

There are three patterns for walls of length 3.

Actually solution is just the fibonacci number fib(length)
"""


import numpy as np


def build_table(length):
    A = np.zeros(length + 1)
    A[0] = 1  # 1 way to have wall of length.0
    A[1] = 1  # 1 way to have wall of length 1
    # This is just fibonnaci sequence
    for i in range(2, length+1):
        A[i] = np.sum(A[i-j] for j in (1, 2))

    return A


def compute_num_patterns(length):
    A = build_table(length)
    return A[length]


def main():
    length = 3
    n = compute_num_patterns(length)
    assert n == 3

    length = 4
    n = compute_num_patterns(length)
    assert n == 5

    length = 5
    n = compute_num_patterns(length)
    assert n == 8


if __name__ == '__main__':
    main()
