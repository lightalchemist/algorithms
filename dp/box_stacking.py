#!/usr/bin/env python

"""
File: box_stacking.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Use DP to solve box stacking problem given in link below.
http://people.cs.clemson.edu/~bcdean/dp_practice/dp_5.swf
"""


import numpy as np


def build_table(widths, depths, heights):
    n = len(widths)
    A = np.zeros(n + 1)
    areas = [w * d for (w, d) in zip(widths, depths)]
    order = sorted(range(n), key=lambda x: areas[x], reverse=True)
    parents = np.zeros(n + 1, dtype=np.int)

    for i in range(1, n+1):
        possible_heights = []
        for j in range(i):  # All boxes that could be a base
            if j == 0:  # First box
                possible_heights.append(heights[order[i-1]])
            elif (widths[order[i-1]] < widths[order[j-1]] and
                  depths[order[i-1]] < depths[order[j-1]]):
                possible_heights.append(A[j] + heights[order[i-1]])
            else:  # Violate constraints
                possible_heights.append(0)  # Impossible.

        j = np.argmax(possible_heights)
        A[i] = possible_heights[j]
        parents[i] = j

    return A, parents, order


def assemble(A, parents, order):
    solution = []
    n = int(np.argmax(A))
    while n > 0:
        solution.append(order[n-1])
        n = parents[n]

    solution.reverse()
    return solution


def opt_ordering(widths, depths, heights):
    A, parents, order = build_table(widths, depths, heights)
    ordering = assemble(A, parents, order)
    return ordering, np.max(A)


def print_solution(solution):
    for i, box in enumerate(solution, 1):
        print("Layer {} | Box {}".format(i, box + 1))


def main():
    widths = [2, 1, 3]
    depths = [2, 1, 3]
    heights = [2, 3, 1]
    solution, opt_height = opt_ordering(widths, depths, heights)
    print_solution(solution)
    print("Opt height: {}".format(opt_height))
    print('-' * 20)

    widths = [2, 1, 3]
    depths = [1, 2, 3]
    heights = [2, 3, 1]
    solution, opt_height = opt_ordering(widths, depths, heights)
    print_solution(solution)
    print("Opt height: {}".format(opt_height))
    print('-' * 20)

    widths = [2, 1, 2]
    depths = [1, 2, 2]
    heights = [2, 3, 4]
    solution, opt_height = opt_ordering(widths, depths, heights)
    print_solution(solution)
    print("Opt height: {}".format(opt_height))
    print('-' * 20)


if __name__ == '__main__':
    main()
