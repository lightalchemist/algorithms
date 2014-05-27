#!/usr/bin/env python

"""
File: num_ways_change.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Compute the number of ways to provide change
for an amount "total" given a set of denominations.
"""

import numpy as np


def build_table(denominations, total):
    """A[i] stores the number of ways to provide change
    for amount i using the given denominations."""
    A = np.zeros(total + 1, dtype=np.int)
    A[0] = 1
    for i in range(min(denominations), total+1):
        A[i] = sum(A[i-v] if v <= i else 0
                   for v in denominations)

    return A


def main():
    denominations = [1, 2]
    C = 3
    A = build_table(denominations, C)
    print("Number of ways to change {} using denominations {}: {}".format(C, denominations, A[-1]))


if __name__ == '__main__':
    main()
