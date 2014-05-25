#!/usr/bin/env python

"""
File: max_val_subsequence.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Computes the maximum value contiguous subsequence
of a given sequence of numbers.
Note that this problem is only interesting if there are negative values
in the given sequence.
"""

import numpy as np


DIS = 0
INC = 1
def build_table(values):
    n = len(values)
    A = np.zeros((n + 1, 2))
    # parent = np.zeros(n + 1, dtype=np.int)
    for i in range(1, n + 1):
        A[i][DIS] = max(A[i-1, :])
        A[i][INC] = max(values[i-1],
                        A[i-1, INC] + values[i-1])
        # if A[i-1] + values[i-1]
        # A[i] = max(A[i-1],
        #            A[i-1] + values[i-1]
        #            )

    return A


def assemble(values, A):
    n = len(values)
    solutions = [None] * (n + 1)
    s = INC if A[n][INC] > A[n][DIS] else DIS
    max_val = A[n][s]
    while n > 0:
        if s == INC:
            solutions[n] = "include"
            max_val -= values[n-1]
        else:
            solutions[n] = "discard"

        s = DIS if A[n-1][DIS] == max_val else INC
        n -= 1

    return solutions[1:]


def main():
    # values = [2, 3, -1, 4, -3]
    values = [2, 3, -4, 4, -3]
    A = build_table(values)
    print(values)
    print(A)
    solutions = assemble(values, A)
    print(solutions)


if __name__ == '__main__':
    main()
