#!/usr/bin/env python

"""
File: knapsack.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: DP solution to knapsack problem.
Solution closely follows pseudocode given in the book
Algorithm Design by Jon Kleinberg and Eva Tardos.

Test cases are taken from
http://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html
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


def knapsack(values, weights, capacity):
    opt = compute_opt_table(values, weights, capacity)
    selected = assemble_solution(opt, values, weights, capacity)
    return selected


def test():
    capacity = 165
    weights = [23,31,29,44,53,38,63,85,89,82]
    values = [92,57,49,68,60,43,67,84,87,72]
    solution = [1,1,1,1,0,1,0,0,0,0]
    solution = [i for i in range(len(solution)) if solution[i] == 1]
    solution = sorted(solution)

    selected = knapsack(values, weights, capacity)
    selected = sorted(selected)
    assert selected == solution

    capacity = 26
    weights = [12,7,11,8,9]
    values = [24,13,23,15,16]
    solution = [0,1,1,1,0]
    solution = [i for i in range(len(solution)) if solution[i] == 1]
    solution = sorted(solution)

    selected = knapsack(values, weights, capacity)
    selected = sorted(selected)
    assert selected == solution

    capacity = 190
    weights = [56,59,80,64,75,17]
    values = [50,50,64,46,50,5]
    solution = [1,1,0,0,1,0]
    solution = [i for i in range(len(solution)) if solution[i] == 1]
    solution = sorted(solution)

    selected = knapsack(values, weights, capacity)
    selected = sorted(selected)
    assert selected == solution

    # capacity = 6404180
    # weights = [382745,799601,909247,729069,467902,44328,34610,698150,823460,
    #            903959,853665,551830,610856,670702,488960,951111,323046,446298,
    #            931161, 31385,496951,264724,224916,169684]
    # values = [825594,1677009,1676628,1523970,943972,97426,69666,1296457,1679693,
    #           1902996,1844992,1049289,1252836,1319836,953277,2067538,675367,853655,
    #           1826027, 65731,901489,577243,466257,369261]
    # solution = [1,1,0,1,1,1,0,0,0,1,1,0,1,0,0,1,0,0,0,0,0,1,1,1]
    # solution = [i for i in range(len(solution)) if solution[i] == 1]
    # solution = sorted(solution)

    # selected = knapsack(values, weights, capacity)
    # selected = sorted(selected)
    # assert selected == solution


if __name__ == '__main__':
    test()
