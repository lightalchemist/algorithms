#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: max_diff.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Computes the maximum difference in a given series of numbers.
"""


from itertools import islice
import numpy as np

from nose.tools import assert_raises

"""
File: max_diff.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Find the maximum positive difference between 2 elements in a given
series of n numbers in O(n) time.
"""


def max_diff(S):
    """Compute max positive difference between 2 elements in a given series of numbers."""
    # Case of 0 or 1 element
    if len(S) <= 1:
        raise ValueError("Series must contain 2 or more elements.")

    min_val = S[0]
    min_idx = 0
    start_idx = min_idx
    end_idx = -1
    max_diff = -np.inf

    for i, s in enumerate(islice(S, 1, len(S)), 1):  # From 2nd element onwards
        if s < min_val:
            min_val = s
            min_idx = i
        else:
            diff = s - min_val
            if diff > max_diff:
                start_idx = min_idx
                end_idx = i
                max_diff = diff

    if end_idx == -1:
        raise ValueError("Series cannot be monotonically decreasing.")

    return max_diff, start_idx, end_idx


def test():
    S = [3, 1, 5]
    d, b, s = max_diff(S)
    assert d == 4
    assert b == 1
    assert s == 2

    S = [4, 1, 2, 5]
    d, b, s = max_diff(S)
    assert d == 4
    assert b == 1
    assert s == 3

    S = [-10, 3, 3, 1]
    d, b, s = max_diff(S)
    assert d == 13
    assert b == 0
    assert s == 1

    S = [-1, 2]
    d, b, s = max_diff(S)
    assert d == 3
    assert b == 0
    assert s == 1

    S = [4, 2, 2, 5, 4, 6, 6]
    d, b, s = max_diff(S)
    assert d == 4
    assert b == 1
    assert s == 5

    assert_raises(ValueError, max_diff, [0, -1, -2])
    assert_raises(ValueError, max_diff, [3])
    assert_raises(ValueError, max_diff, [])


if __name__ == '__main__':
    test()










