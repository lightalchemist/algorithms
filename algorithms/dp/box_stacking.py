#!/usr/bin/env python

"""
File: box_stacking.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Use DP to solve box stacking problem given in link below.
http://people.cs.clemson.edu/~bcdean/dp_practice/dp_5.swf

This solution is wrong as it does not take into account possible rotations...
"""


import numpy as np


def build_table(widths, depths, heights):
    """A[i] is max possible height with box i at the top."""
    n = len(widths)
    A = np.zeros(n + 1)
    areas = [w * d for (w, d) in zip(widths, depths)]
    # Sort according to area in descending order
    order = sorted(range(n), key=lambda x: areas[x], reverse=True)
    parents = np.zeros(n + 1, dtype=np.int)

    # For each box i
    # We are basically searching for all possible box j as base for box i
    # Max height is then max height with box j as top + height of box i.
    # Special case when we don't use any box as base for box i (i.e. j == 0) so
    # height is just height of box i.
    for i in range(1, n+1):  # For each box i
        possible_heights = []
        # All boxes that could potentially be base of box i (i.e. has area < area of box i).
        for j in range(i):  # For each possible base j for box i
            # order[i-1] is idx of box arranged in order of size of area.
            # idea is that if area_i < area_j, then box i can never be base of box j
            # since at least 1 side will not satisfy the necessary constraints.
            if j == 0:  # Box i is first box
                possible_heights.append(heights[order[i-1]])  # Just height of box i.
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
