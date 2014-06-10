#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: longest_consecutive_sum.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Given a sequence of real numbers,
find the longest consecutive sequence that gives the
maximum sum.

Problem taken from Algorithm Design Manual by Steven Skiena 1st Ed.
Qn 3-5 pg 78.

E.g. Given S = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
return [59, 26, -53, 58, 97] with sum = 187.
"""

import numpy as np


def naive_solve(S):
    """ Find max consecutive sum by starting from elements
    i = 0 to n-1 one at a time and ending at some other
    element j where j >= i.

    Time complexity: O(n^2).
    """
    n = len(S)
    start, end = 0, 1
    max_sum = S[0]
    for i in range(n):
        cum_sum = S[i]
        for j in range(i+1, n):
            if cum_sum + S[j] < 0:
                break
            cum_sum += S[j]
            if cum_sum > max_sum:
                max_sum = cum_sum
                start = i
                end = j + 1

    return S[start:end]


def build_table(S):
    """Let A[j] be the max sum S[i:j+1] for some i <= j.
    start[j] = start index of max seq that ends at S[j].

    A[j] = S[j] if A[j-1] < 0 else S[j] + A[j-1]

    The max possible sum = max(A)

    Time complexity: O(n)
    """
    n = len(S)
    start = [0] * n
    A = [0] * n
    A[0] = S[0]  # Base case. Seq with just S[0].
    for j in range(1, n):
        if A[j-1] <= 0:  # Appending S[j] to current seq will be
            A[j] = S[j] # <= starting new seq from S[j]
            start[j] = j  # so we begin new seq at S[j].
        else: # Append S[j] to current seq
            A[j] = S[j] + A[j-1]
            start[j] = start[j-1]  # Seq that ends at j starts from that which

    return A, start


def solve(S):
    A, start = build_table(S)
    j = np.argmax(A)
    return S[start[j]:j+1]


def test():
    S = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
    solution = [59, 26, -53, 58, 97]
    result = naive_solve(S)
    assert solution == result

    result = solve(S)
    assert solution == result

    S = [-1]
    solution = [-1]
    result = solve(S)
    assert solution == result

    S = [2, -1, 1, 5]
    solution = [2, -1, 1, 5]
    result = solve(S)
    assert solution == result

    S = [-1, 1]
    solution = [1]
    result = solve(S)
    assert solution == result

    S = [0, 1]
    solution = [1]
    result = solve(S)
    assert solution == result

    S = [1, 2, 3]
    solution = [1, 2, 3]
    result = solve(S)
    assert solution == result

    S = [100, -99, 1, 0]
    solution = [100]
    result = solve(S)
    assert solution == result

    S = [100, -99, 100, 0]
    solution = [100, -99, 100]
    result = solve(S)
    assert solution == result

    print("All tests pass")


if __name__ == '__main__':
    test()
