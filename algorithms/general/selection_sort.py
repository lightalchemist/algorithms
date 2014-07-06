#!/usr/bin/env python

"""
File: selection_sort.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Implementation of selection sort algorithm.
"""

def sort(seq):
    N = len(seq)
    for i in range(N):
        min_item = float('inf')
        min_idx = i
        # Find min item from i to end and swap into pos i
        for j in range(i, N):
            if seq[j] < min_item:
                min_item = seq[j]
                min_idx = j

        seq[i], seq[min_idx] = seq[min_idx], seq[i]


import copy
import random


def test():
    a = range(10)
    random.shuffle(a)
    b = copy.copy(a)
    sort(a)
    assert a == sorted(b)

    a = [1, 1, 1, 1]
    sort(a)
    assert a == [1, 1, 1, 1]

    a = [-1]
    sort(a)
    assert a == [-1]

    a = [random.randint(-100, 100) for _ in range(100)]
    b = copy.copy(a)
    sort(a)
    assert a == sorted(b)


if __name__ == '__test__':
    test()
