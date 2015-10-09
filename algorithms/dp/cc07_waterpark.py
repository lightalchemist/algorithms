#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: cc07_waterpark.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Solution to problem listed at https://dmoj.ca/problem/ccc07s4
"""



import sys
from collections import defaultdict


def num_paths(x, y, parent_of):
    """Recursive solution. Find number of paths from x to y"""

    # Direct path from x to y, return 1
    if x in parent_of[y]:
        # print("{} is parent of {}".format(x, y))
        return 1 + sum(num_paths(x, p, parent_of) for p in parent_of[y] if p != x)

    # if y has no parent, return 0
    if not parent_of[y]:
        # print("{} not parent of {}".format(x, y))
        return 0

    return sum(num_paths(x, p, parent_of) for p in parent_of[y])


def load_data(filename):
    parent_of = defaultdict(set)
    with open(filename) as infile:
        num_nodes = int(infile.readline())
        for line in infile:
            if line == "0 0":
                break

            x, y = map(int, line.strip().split())
            parent_of[y].add(x)

    return parent_of


def build_matrix(filename, x):
    # A[i] stores number of paths from node x to node i.

    # O(n) to build parents_of_node
    parents_of_node = defaultdict(list)
    with open(filename) as infile:
        num_nodes = int(infile.readline())
        A = [0] * (num_nodes + 1)  # A[0] is dummy variable. Not used.
        for line in infile:
            if line == "0 0":
                break

            u, v = map(int, line.strip().split())
            parents_of_node[v].append(u)

            # Initialize all direct descendants of x to 1
            if u == x:
                A[v] = 1

    # Number of paths from x to i = sum(number of paths from x to parent of i)
    for i in xrange(1, num_nodes + 1):  # O(n)
        A[i] += sum(A[p] for p in parents_of_node[i])  # O(max fan-in of graph), assuming O(1) for accessing dict.

    # Total time complexity to build A is O(n * (max_fan-in of graph))
    return A


def main():
    filename = sys.argv[1]

    x = 1  # Find number of paths from x
    y = 4  # to y
    A = build_matrix(filename, x)
    print(A[y])

    # Recursive solution
    # parents_of_node = load_data(filename)
    # print(parents_of_node)
    # print(A)
    # print(num_paths(x, y, parents_of_node))


if __name__ == "__main__":
    main()
