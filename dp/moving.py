#!/usr/bin/env python

"""
File: consult.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Chap 6 ex 4c of Algorithm Design by Kleinberg and Tardos.
"""

import numpy as np

NY = 0
SF = 1
other = [SF, NY]
def build_table(N, S, moving_cost):
    n = len(N)

    A = np.zeros((n+1, 2))
    for i in range(1, n+1):
        A[i][NY] = min(A[i-1][NY] + N[i-1], A[i-1][SF] + S[i-1] + moving_cost)
        A[i][SF] = min(A[i-1][SF] + S[i-1], A[i-1][NY] + N[i-1] + moving_cost)

    return A


def assemble_plan(N, S, moving_cost, A):
    n = len(N)
    plan = [None] * (n + 1)  # Add 1 dummy slot for clearer indexing.
    loc = SF if A[n][SF] < A[n][NY] else NY
    plan[n] = loc
    while n > 0:
        # Stay at current loc is cheaper than moving from other loc
        if A[n-1][loc] < A[n-1][other[loc]] + moving_cost:
            plan[n-1] = loc
        # Other option is cheaper
        else:
            plan[n-1] = other[loc]
            loc = other[loc]

        n -= 1

    translate = {NY:"NY", SF:"SF"}
    plan = map(translate.get, plan[1:])
    return plan


def main():
    N = [1, 3, 20, 30]
    S = [50, 20, 2, 4]
    moving_cost = 10
    A = build_table(N, S, moving_cost)
    print("Optimal cost: {}".format(np.min(A[-1])))
    plan = assemble_plan(N, S, moving_cost, A)
    print("Optimal plan: {}".format(plan))


if __name__ == '__main__':
    main()
