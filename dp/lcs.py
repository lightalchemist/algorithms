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
    """Computes the table, A[i][j],  needed to reconstruct
    longest common subsequence of string X and Y.
    A[i][j] stores length of longest subsequence between string
    prefixes X[:i] and Y[:j].
    """
    m, n = len(X), len(Y)
    A = np.zeros((m + 1, n + 1), dtype=np.uint)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:  # Common last char.
                A[i][j] = 1 + A[i - 1][j - 1]  # So lcs is this 1 char + lcs of both strings without this last char.
            else:  # Otherwise, lcs is the longer of lcs(X[:i], Y[:j-1]) and lcs(X[:i-1], Y[:j]
                A[i][j] = max(A[i - 1][j], A[i][j - 1])

    return A


def assemble_lcs(A, X, Y, i, j):
    """Reconstruct the longest common subsequence of strings X and Y
    by backtracking through the lcs table."""
    if A[i][j] == 0:  # No common subsequence
        return ""
    elif X[i - 1] == Y[j - 1]:  # Common last char.
        # Append this char to lcs of strings w/o this last char.
        return assemble_lcs(A, X, Y, i - 1, j - 1) + X[i - 1]
    # Else return longer of lcs of one string to another without this last char.
    elif A[i][j - 1] > A[i - 1][j]:
        return assemble_lcs(A, X, Y, i, j - 1)
    else:
        return assemble_lcs(A, X, Y, i - 1, j)


def longest_common_sequence(X, Y):
    """Returns the longest common subsequence of strings X and Y."""
    A = lcs_table(X, Y)
    return assemble_lcs(A, X, Y, len(X), len(Y))


def test():
    X, Y = "XMJYAUZ", "MZJAWXU"
    assert longest_common_sequence(X, Y) == "MJAU"

    X, Y = "ABCDGH", "AEDFHR"
    assert longest_common_sequence(X, Y) == "ADH"

    X, Y = "AGGTAB", "GXTXAYB"
    assert longest_common_sequence(X, Y) == "GTAB"

    X, Y = "", ""
    assert longest_common_sequence(X, Y) == ""

    X, Y = "A", "B"
    assert longest_common_sequence(X, Y) == ""

    X, Y = "", "B"
    assert longest_common_sequence(X, Y) == ""

    X, Y = "thisisatest", "testing123testing"
    assert longest_common_sequence(X, Y) == "tsitest"

    X, Y = "1234", "1224533324"
    assert longest_common_sequence(X, Y) == "1234"


if __name__ == "__main__":
    test()
