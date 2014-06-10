#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: merge_sorted_arrays.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Given 2 sorted arrays A, B, merge
merge them into a sorted array using O(1) additional
storage. Result is stored in A,
assuming A has sufficient storage.

Required time complexity: O(n).
Required space complexity: O(1).

"""

def merge(A, B):
    """Merge sorted arrays A and B into A in O(n) time.
    We first allocate extra space for A to contain B.
    Then start by copying from the ends of original A and B
    into the end of the resized A.
    """
    a = len(A) - 1
    b = len(B) - 1
    A += [None] * len(B)

    write_idx = len(A) - 1
    while write_idx >= 0:
        if a == -1:  # Finished copying from A
            while b >= 0:  # Copy remaining B to A
                A[write_idx] = B[b]
                b -= 1
                write_idx -= 1
            assert write_idx == -1 and b == -1
            break

        if b == -1:  # Finished copying from B
            while a >= 0:  # Copy remaining A into place
                A[write_idx] = A[a]
                a -= 1
                write_idx -= 1
            assert write_idx == -1 and a == -1
            break

        if A[a] > B[b]:
            A[write_idx] = A[a]
            a -= 1
        else:
            A[write_idx] = B[b]
            b -= 1

        write_idx -= 1

    return A


def test():
    A = [2, 3, 5]
    B = [1, 2, 4, 7]
    S = merge(A, B)
    assert S == [1, 2, 2, 3, 4, 5, 7]

    A = []
    B = [1]
    S = merge(A, B)
    assert S == [1]

    A = [1]
    B = []
    S = merge(A, B)
    assert S == [1]

    A = [-2, 0, 5, 7, 9]
    B = [-1, 2, 6, 8]
    S = merge(A, B)
    assert S == [-2, -1, 0, 2, 5, 6, 7, 8, 9]

    B = [-2, 0, 5, 7, 9]
    A = [-1, 2, 6, 8]
    S = merge(A, B)
    assert S == [-2, -1, 0, 2, 5, 6, 7, 8, 9]

if __name__ == '__main__':
    test()
