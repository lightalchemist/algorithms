#!/usr/bin/env python

"""
File: coin_change.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Determine fewest coins from a given set of denominations
needed to provide change for an amount C.
"""


import numpy as np


def build_table(denominations, C):
    """A[i] constains min number of coins needed to change
    value of i.
    C is value we want to change for using coins with values
    in denominations.

    used_coin[i] is denomination used to get value of i.
    """
    A = np.zeros(C + 1, dtype=np.int)
    used_coin = np.zeros(C+1, dtype=np.int)
    for i in range(1, C+1):
        # 1 coin of value denomination + min number needed to change A[i - denomination]
        possible = [(1 + A[i - denomination],
                     denomination)
                    for denomination in denominations
                    if i >= denomination]
        A[i], used_coin[i] = min(possible)

    return A, used_coin


def assemble(C, used_coin):
    coins = []
    while C > 0:
        coins.append(used_coin[C])
        C -= used_coin[C]

    return coins


def print_solution(coins):
    print("Minimum number of coins required: {}".format(
        sum(coins.values())))
    print('-' * 40)
    for value, count in coins.items():
        print("{} x {}".format(count, value))


from collections import Counter
def main():
    denominations = [1, 2, 4, 5, 10]
    C = 29
    A, used_coin = build_table(denominations, C)

    print("Change: {}".format(C))
    print("Denominations: {}".format(denominations))
    coins = assemble(C, used_coin)
    coins = Counter(coins)
    print_solution(coins)


if __name__ == '__main__':
    main()
