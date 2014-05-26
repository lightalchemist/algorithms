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
        # possible = []
        possible = [(1 + A[j], j) if seq[i-1] > seq[j-1] else (1, i) for j in range(i)]
        # for j in range(i):  # Starting from jth position
        #     if seq[i-1] > seq[j-1]:
        #         possible.append((1 + A[j], j))
        #     else:
        #         possible.append((1, i))

        A[i], parent[i] = max(possible)

    return A, parent


def assemble(seq, A, parent):
    subsequence_length = int(np.max(A))
    solution = [None] * (subsequence_length)
    i = np.argmax(A)
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
    solution = [2, 3, 5, 8, 9]

    solution = longest_inc_subsequence(s)
    print("seq: {}".format(s))
    print(solution)

    s = [3, -1]
    solution = longest_inc_subsequence(s)
    print("seq: {}".format(s))
    print(solution)

    s = [-1]
    solution = longest_inc_subsequence(s)
    print("seq: {}".format(s))
    print(solution)


if __name__ == '__main__':
    main()
