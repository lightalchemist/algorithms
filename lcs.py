#!/usr/bin/env python

"""
File: lcs.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Implements the longest common subsequence algorithm using DP.
Implementation follows pseudocode given in the book: Algorithms Unlocked by Thomas Cormen.
"""

import numpy as np


def lcs_table(X, Y):
    """Computes the least common subsequence of string X and Y."""
    m, n = len(X), len(Y)

    A = np.zeros((m+1, n+1), dtype=np.uint)
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                A[i][j] = 1 + A[i-1][j-1]
            else:
                A[i][j] = max(A[i-1][j], A[i][j-1])

    return A


def assemble_lcs(A, X, Y, i, j):
    if A[i][j] == 0:
        return ""
    elif X[i-1] == Y[j-1]:
        return assemble_lcs(A, X, Y, i-1, j-1) + X[i-1]
    elif A[i][j-1] > A[i-1][j]:
        return assemble_lcs(A, X, Y, i, j-1)
    else:
        return assemble_lcs(A, X, Y, i-1, j)


def longest_common_sequence(X, Y):
    A = lcs_table(X, Y)
    return assemble_lcs(A, X, Y, len(X), len(Y))


def test():
    X = "XMJYAUZ"
    Y = "MZJAWXU"
    assert longest_common_sequence(X, Y) == "MJAU"

    X = "ABCDGH"
    Y = "AEDFHR"
    assert longest_common_sequence(X, Y) == "ADH"

    X = "AGGTAB"
    Y = "GXTXAYB"
    assert longest_common_sequence(X, Y) == "GTAB"

    X = ""
    Y = ""
    assert longest_common_sequence(X, Y) == ""

    X = "A"
    Y = "B"
    assert longest_common_sequence(X, Y) == ""

    X = ""
    Y = "B"
    assert longest_common_sequence(X, Y) == ""


if __name__ == "__main__":
    test()
