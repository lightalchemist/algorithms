#!/usr/bin/env python

"""
File: dice_throw.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description:
    Suppose you are given 'n' dice, each with 'm' faces.
    So the faces of the die takes on exactly one value in the range [1, m].
    You are also given a value 's'.
    Determine the number of ways to obtain 's' as the sum of the n dice.

Details of the problem can be found at: http://www.geeksforgeeks.org/dice-throw-problem/
"""

import numpy as np


def memo(f):
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            value = f(*args)
            cache[args] = value
            return value
        except TypeError:
            return f(*args)

    return _f


@memo
def n_ways_recursive(s, n, m):
    """Recursive solution for the given problem."""
    if s < n:
        return 0
    elif n == 1 and s <= m:
        return 1
    else:
        return sum(n_ways_recursive(s-i, n-1, m) for i in range(1, m+1))


def n_ways_dp(s, n, m):
    """Computes the number of ways to get a sum of 's'
    from the value of 'n' dice each with 'm' faces.
    A[i][j] stores the number of ways to get a sum of 'j'
    by throwing 'i' dice each with 'm' faces."""
    A = np.zeros((n+1, s+1), dtype=np.uint)
    for j in range(1, min(s+1, m+1)):  # Only 1 way to get score of 's' with 1 die if largest value is m.
        A[1][j] = 1

    for i in range(2, n+1):  # Start from case of 2 dice since 1 die case taken care of already.
        for j in range(i, s+1):  # Sum must be at least the number of dice 'i' we are throwing.
            A[i][j] = sum((A[i-1][j-roll]) for roll in xrange(1, min(j+1, m+1)))

    print(A)
    return A[n][s]  # Number of ways to get 's' from 'n' dice.


def test():
    assert n_ways_recursive(2, 3, 6) == 0
    assert n_ways_recursive(3, 3, 6) == 1
    assert n_ways_recursive(4, 3, 6) == 3

    assert n_ways_recursive(8, 3, 6) == 21
    assert n_ways_recursive(5, 3, 4) == 6
    assert n_ways_recursive(5, 2, 4) == 4
    # assert n_ways_recursive(8, 3, 6) == 21

    assert n_ways_dp(2, 3, 6) == 0
    assert n_ways_dp(3, 3, 6) == 1
    assert n_ways_dp(4, 3, 6) == 3
    assert n_ways_dp(8, 3, 6) == 21
    assert n_ways_dp(5, 3, 4) == 6
    assert n_ways_dp(5, 2, 4) == 4

if __name__ == '__main__':
    test()
