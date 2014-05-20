#!/usr/bin/env python

from collections import defaultdict
import numpy as np


def sequence_alignment_table(X, Y, gap_cost, mismatch_cost):
    m, n = len(X), len(Y)
    A = np.zeros((m + 1, n + 1), dtype=np.uint)

    for i in range(m + 1):
        A[i][0] = i*gap_cost
    for j in range(n + 1):
        A[0][j] = j*gap_cost

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                m_cost = 0
            else:
                m_cost = mismatch_cost[(X[i - 1], Y[j - 1])]

            A[i][j] = min(m_cost + A[i - 1][j - 1],
                          gap_cost + A[i][j - 1],
                          gap_cost + A[i - 1][j])

    return A


gap_symb = '_'
def assemble2(A, X, Y, i, j):
    if i < 0 and j < 0:
        return "", ""

    if i < 0 and j >= 0:
        # return gap_symb * (j + 1), Y[:j+1]
        return gap_symb * (j + 1), Y[:j+1]
        # return gap_symb * (j), Y[:j]
    if j < 0 and i >= 0:
        # return X[:i+1], gap_symb * (i + 1)
        return X[:i+1], gap_symb * (i + 1)
        # return X[:i], gap_symb * (i)

    if X[i-1] == Y[j-1]:  # Same. No cost.
        Xi, Yi = assemble(A, X, Y, i-1, j-1)
        return Xi + X[i-1], Yi + Y[j-1]

    if A[i-1][j-1] < A[i][j-1] and A[i-1][j-1] < A[i-1][j]:  # mismatch
        Xi, Yi = assemble(A, X, Y, i-1, j-1)
        return Xi + X[i-1], Yi + Y[j-1]

    if A[i][j-1] < A[i-1][j]:
        Xi, Yi = assemble(A, X, Y, i, j-1)
        return Xi + gap_symb, Yi + Y[j-1]
    else:
        Xi, Yi = assemble(A, X, Y, i-1, j)
        return Xi + X[i-1], Yi + gap_symb


import pdb
def assemble(A, X, Y, u, v):
    i, j = len(X), len(Y)
    x = ""
    y = ""
    while i > 0 and j > 0:

        if A[i-1][j-1] < A[i-1][j] and A[i-1][j-1] < A[i][j-1]:
            x = X[i-1] + x
            y = Y[j-1] + y
            i -= 1
            j -= 1

        elif A[i][j-1] < A[i-1][j]:
            x = gap_symb + x
            y = Y[j-1] + y
            j -= 1

        else:
            x = X[i-1] + x
            y = gap_symb + y
            i -= 1


    # pdb.set_trace()
    if i > 0:
        y = gap_symb * (i) + y
        x = X[:i] + x

    if j > 0:
        x = gap_symb * (j) + x
        y = Y[:j] + y

    return x, y


def align(X, Y, gap_cost, mismatch_cost):
    A = sequence_alignment_table(X, Y, gap_cost, mismatch_cost)
    print(A)
    sx, sy = assemble(A, X, Y, len(X), len(Y))
    print (X)
    print(Y)
    print('-' * max(len(X), len(Y)))
    print(sx)
    print(sy)


def test():
    gap_cost = 1
    MISMATCH_COST = defaultdict(lambda: 2)

    X, Y = "stop", "tops"
    X, Y = "bus stop", "top"
    X, Y = "atop", "top"
    X, Y = "atop", "top-class"

    align(X, Y, gap_cost, MISMATCH_COST)


if __name__ == '__main__':
    test()
