#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
from nose.tools import assert_raises


def max_consecutive_diff(S):
    """Computes the maximum difference between the start and end of
    a consecutive increasing subsequence among all consecutive increasing subsequences
    of a series of numbers S.

    Raises ValueError if S has <= 1 elements.
    Algorithm returns max difference along with start and end indices of elements of first consecutive
    increasing subsequence it encounters with the max difference.
    """

    if len(S) <= 1:
        raise ValueError("Series must have at least 2 elements.")

    diff = 0
    max_diff = -np.inf
    start_idx = 0
    end_idx = -1
    cur_start_idx = start_idx
    for i in range(1, len(S)):
        if S[i] >= S[i-1]:  # Inc seq continues.
            diff += S[i] - S[i-1]
            if diff > max_diff:  # Check if prev inc seq has > max diff than cur max diff.
                max_diff = diff
                start_idx = cur_start_idx
                end_idx = i
        else: # Start of new seq
            diff = 0
            cur_start_idx = i

    if end_idx == -1:
        raise ValueError("Series cannot be monotonically decreasing.")

    return max_diff, start_idx, end_idx


def test():
    S = [1, 1]
    d, i, j  = max_consecutive_diff(S)
    assert d == 0
    assert S[j] - S[i] == d
    assert i == 0 and j == 1

    S = [3, 3]
    d, i, j = max_consecutive_diff(S)
    assert d == 0
    assert S[j] - S[i] == d
    assert i == 0 and j == 1

    S = [1, 2]
    d, i, j  = max_consecutive_diff(S)
    assert d == 1
    assert S[j] - S[i] == d
    assert i == 0 and j == 1

    S = [1, 2, 3]
    d, i, j  = max_consecutive_diff(S)
    assert d == 2
    assert S[j] - S[i] == d
    assert i == 0 and j == 2

    S = [2, 1, 2]
    d, i, j  = max_consecutive_diff(S)
    assert d == 1
    assert S[j] - S[i] == d
    assert i == 1 and j == 2

    S = [3, 2, 2, 4, 2, 1, 2, 2, 7, 6]
    d, i, j  = max_consecutive_diff(S)
    assert d == 6
    assert S[j] - S[i] == d
    assert i == 5 and j == 8

    S = [3, 2, 2, 4, 2, 1, 2, 2, 7, 7]
    d, i, j  = max_consecutive_diff(S)
    assert d == 6
    assert S[j] - S[i] == d
    assert i == 5 and j == 8

    S = [3, 2, 2, 4, 8, 1, 2, 2, 7, 7]
    d, i, j  = max_consecutive_diff(S)
    assert d == 6
    assert S[j] - S[i] == d
    assert i == 1 and j == 4

    assert_raises(ValueError, max_consecutive_diff, [])
    assert_raises(ValueError, max_consecutive_diff, [3])
    assert_raises(ValueError, max_consecutive_diff, [3, 2])


if __name__ == '__main__':
    test()
