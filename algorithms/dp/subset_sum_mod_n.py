#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: subset_sum_mod_n.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Given sequence of n numbers, find the subset whose sum
modulus n == 0.
"""

import numpy as np


def build_table2(V, n):
    """A[i][v] = min number of numbers needed to sum to v"""
    A = np.zeros((len(V) + 1, n + 1), dtype=np.int)
    for i in range(1, A.shape[0]):
        for v in range(1, A.shape[1]):
            if V[i-1] == v:
                A[i][v] = 1
            elif V[i-1] > v:  # Cannot use vi
                A[i][v] = A[i-1][v]
            else:
                if A[i-1][v] > 0 and A[i-1][v-V[i-1]] > 0:
                    A[i][v] = min(A[i-1][v], A[i-1][v - V[i-1]] + 1)
                elif A[i-1][v] > 0:
                    A[i][v] = A[i-1][v]
                else:
                    A[i][v] = A[i-1][v - V[i-1]]

                # A[i][v] = min(A[i-1][v], A[i-1][v - V[i-1]] + 1)

    return A


def assemble2(V, A):
    m, n = A.shape



def build_table(V, n):
    """A[i][v] = 1 if first i elements can sum to v."""

    A = np.zeros((len(V) + 1, n + 1), dtype=np.int)
    for i in range(1, A.shape[0]):
        for v in range(1, A.shape[1]):
            if V[i-1] == v or A[i-1][v - V[i-1]]:
                A[i][v] = 1  # Use vi
            elif V[i-1] > v and A[i-1][v]:
                A[i][v] = 1  # Don't use vi
            else:  # Don't use vi
                A[i][v] = 0  # vi not used in subset to v

    return A


def assemble(A, V):
    n = A.shape[1] - 1
    m = len(V)
    if A[m][n] == 0:  # No solution
        return []

    v = n
    i = m
    solution = []
    while i > 0 and v > 0:
        if (V[i-1] == v or
            V[i-1] <= v and A[i-1][v - V[i-1]]):
            solution.append(i-1)
            v -= V[i-1]
        # elif V[i-1] <= v and A[i-1][v - V[i-1]]:
        #     solution.append(i-1)
        #     v -= V[i-1]

        i -= 1

    return solution


def solve(X):
    n = len(X)
    remainders = [x % n for x in X]
    A = build_table(remainders, n)
    return assemble(A, remainders)


def test():
    X = [429, 334, 62, 711, 704, 763, 98, 733, 721, 995]
    # subsets = solve(X)
    # print(subsets)
    # print([X[i] for i in subsets])
    # assert sum(X[i] for i in subsets) % len(X) == 0
    A = build_table2(X, len(X))
    print(A)

    # X = [1, 2, 3]
    # A = build_table(X, 1)
    # print(A)
    # solution = assemble(A, X)
    # print([X[i] for i in solution])
    # print('-' * 30)

    # A = build_table(X, 2)
    # print(A)
    # solution = assemble(A, X)
    # print([X[i] for i in solution])
    # print('-' * 30)

    # A = build_table(X, 3)
    # print(A)
    # solution = assemble(A, X)
    # print([X[i] for i in solution])
    # print('-' * 30)

    # A = build_table(X, 4)
    # print(A)
    # solution = assemble(A, X)
    # print([X[i] for i in solution])
    # print('-' * 30)

    # A = build_table(X, 5)
    # print(A)
    # solution = assemble(A, X)
    # print([X[i] for i in solution])
    # print('-' * 30)

    # A = build_table(X, 6)
    # print(A)
    # solution = assemble(A, X)
    # print([X[i] for i in solution])
    # print('-' * 30)

    # s = 7
    # A = build_table(X, s)
    # print(A)
    # print("X: {}".format(X))
    # print("sum: {}".format(s))
    # solution = assemble(A, X)
    # print([X[i] for i in solution])
    # print('-' * 30)


if __name__ == '__main__':
    test()
