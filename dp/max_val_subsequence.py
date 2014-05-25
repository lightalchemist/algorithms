#!/usr/bin/env python

"""
File: max_val_subsequence.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Computes the maximum value contiguous subsequence
of a given sequence of numbers.
Note that this problem is only interesting if there are negative values
in the given sequence.
"""

import numpy as np


def build_table(values):
    n = len(values)
    A = np.zeros(n + 1)
    parent = [None] * (n + 1)
    parent[0] = 1
    for i in range(1, n + 1):
        if values[i-1] > A[i-1] + values[i-1]:
            A[i] = values[i-1]
            parent[i] = i
        else:
            A[i] = A[i-1] + values[i-1]
            parent[i] = parent[i-1]

    return A, parent

def assemble(values, A, parent):
    j = np.argmax(A)
    return (parent[j], j), values[parent[j]-1:j]


def max_val_subsequence(values):
    A, parent = build_table(values)
    idxs, subsequence = assemble(values, A, parent)
    return subsequence


def main():
    values = [2, 3, -1, 4, -3]
    subsequence = max_val_subsequence(values)
    assert subsequence == [2, 3, -1, 4]

    values = [2, 3, -3, 4, -3]
    subsequence = max_val_subsequence(values)
    assert subsequence == [2, 3, -3, 4]

    values = [-2]
    subsequence = max_val_subsequence(values)
    assert subsequence == []

    values = [3, -1]
    subsequence = max_val_subsequence(values)
    assert subsequence == [3]

    values = [1, -2]
    subsequence = max_val_subsequence(values)
    assert subsequence == [1]

    values = [1, -2, 5, -6, 10]
    subsequence = max_val_subsequence(values)
    assert subsequence == [10]


if __name__ == '__main__':
    main()
