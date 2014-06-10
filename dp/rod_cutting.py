#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: rod_cutting.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Rod cutting question from
Introduction to Algorithm by Cormen et al.

Given rod of length n inches and list of prices
pi, for i = 1, 2, ..., n, determine the max revenue rn
obtainable by cutting up the rod and selling the pieces.

Note that if pn for the rod is large enough, an optimal
solution may require no cutting at all.

"""


import numpy as np


def build_table(n, prices):
    A = np.empty(n+1, np.uint)
    A[0] = 0
    A[1] = prices[0]  # Length 1
    cut_at = [None] * (n+1)
    cut_at[1] = 1
    for i in range(2, n+1):
        possible = [(prices[j-1] + A[i-j], j)  # Cut at j
                    for j in range(1, i)]
        possible.append((prices[i-1], i))  # No cut
        A[i], cut_at[i] = max(possible)


        # A[i] = max(prices[i-1],  # No cut. Sell at price pi.
        #            *[prices[j-1] + A[i-j]  # Cut from 1 to just short of i
        #              for j in range(1, i)])

    return A, cut_at


def assemble(n, cut_at):
    solution = []
    while n != cut_at[n]:
        solution.append(cut_at[n])
        n = cut_at[n]

    solution = list(reversed(solution))
    return solution


def max_revenue(n, prices):
    A, cut_at = build_table(n, prices)
    solution = assemble(n, cut_at)
    return A[n], solution


def print_solution(n, cut_at, prices, revenue):
    print("Given rod of length {}".format(n))
    for c in cut_at:
        length = n - c
        line = "Cut at {} to get length {}" \
            " and sell for price {}".format(c,
                                            length,
                                            prices[length-1])
        print(line)
        n = c

    if len(cut_at) > 1:
        line = "Selling remaining length {} for price {}".format(n, prices[n-1])
    else:
        line = "Don't cut. Sell entire length {} for price {}".format(n, prices[n-1])

    print(line)
    print("")
    print("Total revenue: {}".format(revenue))



def test():
    prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    n = 10
    # print("Prices: {}".format(prices))
    revenue, cut_at = max_revenue(n, prices)
    assert cut_at == []
    assert revenue == 30
    print_solution(n, cut_at, prices, revenue)

    n = 7
    revenue, cut_at = max_revenue(n, prices)
    assert cut_at == [6]
    assert revenue == 18
    print_solution(n, cut_at, prices, revenue)

    n = 3
    revenue, cut_at = max_revenue(n, prices)
    assert cut_at == []
    assert revenue == 8
    print_solution(n, cut_at, prices, revenue)

    n = 4
    revenue, cut_at = max_revenue(n, prices)
    assert cut_at == [2]
    assert revenue == 10
    print_solution(n, cut_at, prices, revenue)


if __name__ == '__main__':
    test()
