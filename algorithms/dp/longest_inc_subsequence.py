#!/usr/bin/env python

"""
File: longest_inc_subsequence.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Solves longest inc subseqence problem.
"""

import numpy as np


def build_table(seq):
    n = len(seq)
    A = np.zeros(n+1)
    parent = np.zeros(n+1, dtype=int)

    # Max subsequence length of first char is just 1 i.e. seq containing just itself.
    A[1] = 1
    # Parent of first char in seq is itself.
    parent[1] = 1
    for i in range(2, n+1):  # Max inc subsequence length ending at ith position.
        # Possible len of subsequences starting at position j ending at position i if conditions satistified.
        possible = [(1 + A[j], j) if seq[i-1] > seq[j-1]  # Max len is 1 + A[j] starting at position j
                    else (1, i)  # Max len is 1 with subsequence just char i
                    for j in range(1, i)]  # For each starting position j

        A[i], parent[i] = max(possible)

    return A, parent


def assemble(seq, A, parent):
    subsequence_length = int(np.max(A))
    solution = [None] * (subsequence_length)
    i = np.argmax(A)  # Idx of last char in seq.
    # Backtrack from last char.
    for j in range(subsequence_length-1, -1, -1):
        solution[j] = seq[i-1]
        i = parent[i]

    return solution


def longest_inc_subsequence(seq):
    A, parent = build_table(seq)
    solution = assemble(seq, A, parent)
    return solution


def main():
    s = [7, 2, 3, 1, 5, 8, 9, 6]

    solution = longest_inc_subsequence(s)
    print("seq: {}".format(s))
    assert solution == [2, 3, 5, 8, 9]
    print(solution)

    s = [3, -1]
    solution = longest_inc_subsequence(s)
    print("seq: {}".format(s))
    assert solution == [3]
    print(solution)

    s = [-1]
    solution = longest_inc_subsequence(s)
    print("seq: {}".format(s))
    assert solution == [-1]
    print(solution)


if __name__ == '__main__':
    main()
