#!/usr/bin/env python

"""
File: hg_fargo.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Problem 7-2 of MIT 6.006 problem set 7
"""

import numpy as np


def build_table(total, start, end):
    A = np.zeros(total + 1, dtype=np.int)
    invested = np.zeros(total + 1, dtype=np.int)
    for t in range(1, total+1):
        possible = []
        for i, (s, e) in enumerate(zip(start, end)):
            profit = e-s
            if t >= s:
                possible.append((A[t-s] + profit, i))  # Buy stock i
            else:
                possible.append((t, -1))

        A[t], invested[t] = max(possible)

    return A, invested


def assemble(total, start, invested):
    solution = []
    min_stock_price = min(start)
    while total > 0:
        if total < min_stock_price:
            solution.append("Keep " + str(total))
            break

        solution.append(invested[total])
        total -= start[invested[total]]

    return solution


def main():
    start = [12, 10, 18, 15]
    end = [39, 13, 47, 45]
    total = 30

    A, invested = build_table(total, start, end)
    solution = assemble(total, start, invested)

    print(A)
    print(invested)
    print(A[total])
    print(solution)


if __name__ == '__main__':
    main()
