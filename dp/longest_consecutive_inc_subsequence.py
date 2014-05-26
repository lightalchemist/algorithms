#!/usr/bin/env python

"""
File: longest_consecutive_inc_subsequence.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Longest consecutive increasing subsequence.
Given a sequence s, finds the longest substring where consecutive
numbers are in increasing order.
E.g.
    s = [7, 2, 3, 1, 5, 8, 9, 6]
    solution = [1, 5, 8, 9]

    s = [-1, -3, 0, 1]
    solution = [-3, 0, 1]

    s = [3, 4, 4, 2, 5]
    solution = [3, 4]

"""

import numpy as np


def build_table(seq):
    n = len(seq)
    A = np.zeros(n+1, dtype=np.int)
    parents = np.zeros(n+1, dtype=np.int)
    A[1] = 1
    parents[1] = 1
    for i in range(2, n+1):
        if seq[i-1] <= seq[i-2]:
            A[i] = 1
            parents[i] = i
        else:
            A[i] = A[i-1] + 1
            parents[i] = parents[i-1]

    return A, parents


def assemble(seq, A, parents):
    i = np.argmax(A)
    return seq[parents[i]-1:i]


def longest_inc_sub(seq):
    A, parents = build_table(seq)
    return assemble(seq, A, parents)


def main():
    s = [7, 2, 3, 1, 5, 8, 9, 6]
    solution = longest_inc_sub(s)
    print("Seq: {}".format(s))
    print("Solution: {}".format(solution))
    assert solution == [1, 5, 8, 9]

    s = [2, 3, -1, 4, 5, 6, 3, 7]
    solution = longest_inc_sub(s)
    print("Seq: {}".format(s))
    print("Solution: {}".format(solution))
    assert solution == [-1, 4, 5, 6]

    s = [-1, -3, 0, 1]
    solution = longest_inc_sub(s)
    print("Seq: {}".format(s))
    print("Solution: {}".format(solution))
    assert solution == [-3, 0, 1]

    s = [3, 4, 4, 2, 5]
    solution = longest_inc_sub(s)
    print("Seq: {}".format(s))
    print("Solution: {}".format(solution))
    assert solution == [3, 4]

if __name__ == '__main__':
    main()
