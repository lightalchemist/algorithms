#!/usr/bin/env python

"""
File: knapsack.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: DP solution to knapsack problem.
Solution closely follows pseudocode given in the book
Algorithm Design by Jon Kleinberg and Eva Tardos.
"""


import numpy as np


def compute_opt_table(values, weights, capacity):
    """Computes table of optimal values for knapsack subproblems.
    Total time complexity is O(nW) where n is number of items and W is capacity."""
    n = len(values)
    opt = np.zeros((n+1, capacity+1), dtype=np.uint)

    for i in range(1, n+1):
        for w in range(1, capacity+1):
            if w < weights[i-1]:  # Not enough capacity left to take item
                opt[i][w] = opt[i-1][w]  # Skip item
            else:
                opt[i][w] = max(opt[i-1][w],  # Don't take item
                                values[i-1] + opt[i-1][w - weights[i-1]])  # Take item

    return opt


def assemble_solution(opt, values, weights, capacity):
    i = len(values)  # Number of items.
    selected = []
    while i > 0 and capacity > 0:
        # If taking results in greater value, take item
        if (capacity >= weights[i-1] and
            values[i-1] + opt[i-1][capacity - weights[i-1]] > opt[i-1][capacity]):

            capacity -= weights[i-1]  # Reduce capacity after taking item
            selected.append(i-1)

        i -= 1

    return selected


def test():
    capacity = 165
    weights = [23,31,29,44,53,38,63,85,89,82]
    values = [92,57,49,68,60,43,67,84,87,72]
    selected = [1,1,1,1,0,1,0,0,0,0]
    selected = [i for i in range(len(selected)) if selected[i] == 1]
    print(selected)

    opt = compute_opt_table(values, weights, capacity)
    print("Optimal value: {}".format(opt[len(values)][capacity]))

    selected = assemble_solution(opt, values, weights, capacity)
    print(selected)


if __name__ == '__main__':
    test()
