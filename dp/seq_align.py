#!/usr/bin/env python

"""
File: seq_align.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Performs sequence alignment of 2 strings.
Code is based on pseudocode given in the book
Algorithm Design by Jon Kleinberg and Eva Tardos
"""

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
            if X[i-1] == Y[j-1]:
                m_cost = 0
            else:
                m_cost = mismatch_cost[(X[i-1], Y[j-1])]

            A[i][j] = min(m_cost + A[i-1][j-1],
                          gap_cost + A[i][j-1],
                          gap_cost + A[i-1][j])

    return A


def assemble(A, X, Y):
    GAP_SYMBOL = '_'
    i, j = len(X), len(Y)
    aligned_X, aligned_Y = "", ""
    while i > 0 and j > 0:
        # Eact match or mismatch
        if A[i-1][j-1] < A[i-1][j] and A[i-1][j-1] < A[i][j-1]:
            aligned_X = X[i-1] + aligned_X
            aligned_Y = Y[j-1] + aligned_Y
            i -= 1
            j -= 1
        # Cheaper to leave a gap for X
        elif A[i][j-1] < A[i-1][j]:
            aligned_X = GAP_SYMBOL + aligned_X
            aligned_Y = Y[j-1] + aligned_Y
            j -= 1
        # Cheaper to leave a gap for Y
        else:
            aligned_X = X[i-1] + aligned_X
            aligned_Y = GAP_SYMBOL + aligned_Y
            i -= 1

    # Add gaps to pad remaining chars from X
    if i > 0:
        aligned_Y = GAP_SYMBOL*i + aligned_Y
        aligned_X = X[:i] + aligned_X

    # Add gaps to pad remaining chars from Y
    if j > 0:
        aligned_X = GAP_SYMBOL*j + aligned_X
        aligned_Y = Y[:j] + aligned_Y

    return aligned_X, aligned_Y


def align(X, Y, gap_cost, mismatch_cost):
    A = sequence_alignment_table(X, Y, gap_cost, mismatch_cost)
    aligned_X, aligned_Y = assemble(A, X, Y)
    alignment_cost = A[len(X), len(Y)]

    print('-' * max(len(X), len(Y)))
    print("Given strings: ")
    print (X)
    print(Y)
    print('-' * max(len(X), len(Y)))
    print("Aligned strings: ")
    print(aligned_X)
    print(aligned_Y)
    print("Cost: {}".format(alignment_cost))


def test():
    gap_cost = 1
    # Dictionary of mismatch cost. Default cost currently set to 2.
    # Consider implementing as an array instead for faster access.
    MISMATCH_COST = defaultdict(lambda: 2)

    X, Y = "stop", "tops"
    X, Y = "bus stops here", "top"
    X, Y = "atop", "top"
    X, Y = "atop", "top-class"
    X, Y = "jennifer aniston", "angelina jolie"
    X, Y = "tom hanks is sam", "tom cruise robs bank"
    X, Y = "gold digger", "rube goldberg"
    X, Y = "will smith in mib", "smithsonian museums"

    align(X, Y, gap_cost, MISMATCH_COST)


if __name__ == '__main__':
    test()
