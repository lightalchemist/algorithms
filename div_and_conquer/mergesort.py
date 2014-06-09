#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
File: mergesort.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Implementation of the mergesort algorithm.
Time complexity: O(nlogn)
"""


def merge(A, B):
    """This is just the merge algorithm for mergesort.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    C = [None] * (len(A) + len(B))
    i = j = k = 0
    while i < len(C):
        if j == len(A):  # Reached end of A
            # Copy remaining of B to C
            while k < len(B):
                C[i] = B[k]
                k += 1
                i += 1
            break

        if k == len(B):  # Reached end of B
            # Copy remaining of A to C
            while j < len(A):
                C[i] = A[j]
                j += 1
                i += 1
            break

        if A[j] < B[k]:
            C[i] = A[j]  # Copy from A
            j += 1
        else:
            C[i] = B[k]  # Coy from B
            k += 1

        i += 1

    return C


def sort(S):
    """Implementation of merge sort.
    Time complexity: O(nlogn)
    Space complexity: O(n)
    """

    if len(S) <= 1:
        return S

    mid = len(S) // 2
    A = sort(S[:mid])
    B = sort(S[mid:])
    S = merge(A, B)

    return S


import random


def test():

    A = [2, 2, 3, 4]
    B = [1, 2, 3, 5, 6]
    C = merge(A, B)
    assert C == [1, 2, 2, 2, 3, 3, 4, 5, 6]

    A = [-1, 3, 10, 10]
    B = [-5, -1, 5, 9, 11]
    C = merge(A, B)
    assert C == [-5, -1, -1, 3, 5, 9, 10, 10, 11]

    A = []
    B = [1, 2]
    C = merge(A, B)
    assert C == [1, 2]

    S = []
    S_sorted = sort(S)
    assert S_sorted == []

    S = [2, 2, -1, -1, 3, 10, 100]
    S_sorted = sort(S)
    assert S_sorted == sorted(S)

    S = [2, 3, -1, 0, 5]
    S_sorted = sort(S)
    assert S_sorted == sorted(S)

    S = range(20)
    random.shuffle(S)
    S_sorted = sort(S)
    assert S_sorted == sorted(S)


if __name__ == '__main__':
    test()
