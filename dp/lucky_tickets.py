#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: lucky_tickets.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Problem taken from
http://acm.timus.ru/problem.aspx?space=1&num=1036

You are given a number 1 <= N <= 50.
Every ticket has its 2N-digit number.

We call a ticket lucky,
if the sum of its first N digits is equal to the sum of its last N digits.

You are also given the sum of ALL digits in the number.
Your task is to count an amount of lucky numbers,
having the specified sum of ALL digits.

0 <= S <= 1000

Input
Two space-separated numbers: N and S. Here S is the sum of all digits. Assume that 0 ≤ S ≤ 1000.
Output
The amount of lucky tickets.

Sample input:
    N=2 S=2

Sample output:
    4

The tickets are 0101, 0110, 1001, 1010 in the example above
"""


import numpy as np


def build_table(N, V):
    """A[i][v] = number of ways to have i digits (i = 1,...,N) sum to v
    v = 0,...,V"""
    # By default, 0 ways to have 0 digits sum to anything.
    A = np.zeros((N+1, V+1))
    # 1 way to have 1 digit have sum = 0, 1, ..., min(9, V+1)
    A[1, 0:min(9, V+1)] = 1
    for i in range(2, N+1):  # For 2 digits onwards
        # Max value is min of {number of digits * 9, V}
        for v in range(0, min(i*9 + 1, V+1)):
            # Num ways to use i digits to sum to v is
            # num ways to use (i-1) digits to sum to v-j and have ith digit
            # equal to j where j = 0, 1, ..., up to 9 or v, whichever is smaller
            A[i][v] = np.sum(A[i-1][v-j]
                             for j in range(min(10, v+1)))

    return A


def compute_num_lucky_tickets(N, S):
    """Number of ways for 2N digits to sum to S with sum of first N digits
    equal to sum of last N digits is same as number of ways, m, for first N
    digits to sum to S//2, each combined with number of ways for last N digits
    to sum to S//2. Hence the total number of ways is m^2."""
    A = build_table(N, S//2)
    print(A)
    m = A[N, S//2]**2
    return m**2


def main():
    N = 2
    S = 2
    n = compute_num_lucky_tickets(N, S)
    assert n == 4
    print("N: {} S: {}".format(N, S))
    print(n)

    N = 2
    S = 4
    n = compute_num_lucky_tickets(N, S)
    assert n == 9
    print("N: {} S: {}".format(N, S))
    print(n)

    N = 2
    S = 6
    n = compute_num_lucky_tickets(N, S)
    assert n == 16
    print("N: {} S: {}".format(N, S))
    print(n)

    N = 2
    S = 8
    n = compute_num_lucky_tickets(N, S)
    assert n == 25
    print("N: {} S: {}".format(N, S))
    print(n)


if __name__ == '__main__':
    main()
