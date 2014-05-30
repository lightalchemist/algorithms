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


def build_table(C, denominations):
    """A[i] constains min number of coins needed to change
    value of i.
    C is value we want to change for using coins with values
    in denominations.

    used_coin[i] is denomination used to get value of i.
    """
    A = np.zeros(C + 1, dtype=np.int)
    used_coin = np.zeros(C+1, dtype=np.int)
    for i in range(1, C+1):
        # 1 coin of value denomination + min number needed to change
        # A[i - denomination]
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
    """coins is a Counter/dict object with denominations as keys
    and the number of coins for each denomination as values."""
    print("Minimum number of coins required: {}".format(
        sum(coins.values())))
    print('-' * 40)
    for value, count in coins.items():
        print("{} x {}".format(count, value))


def make_change(C, denominations):
    """Return number of coins for each denominations needed to make change C.
    C is amount to change for.
    denominations is list of integer denominations.
    """
    A, used_coin = build_table(C, denominations)
    coins = assemble(C, used_coin)
    return Counter(coins)


from collections import Counter
def main():
    denominations = [1, 2, 4, 5, 10]
    C = 29
    print("Change: {}".format(C))
    print("Denominations: {}".format(denominations))
    coins = make_change(C, denominations)
    assert sum(coins.values()) == 4
    print_solution(coins)

    C = 20
    print("Change: {}".format(C))
    print("Denominations: {}".format(denominations))
    coins = make_change(C, denominations)
    assert sum(coins.values()) == 2
    print_solution(coins)

    C = 2
    print("Change: {}".format(C))
    print("Denominations: {}".format(denominations))
    coins = make_change(C, denominations)
    assert sum(coins.values()) == 1
    print_solution(coins)

    C = 12
    print("Change: {}".format(C))
    print("Denominations: {}".format(denominations))
    coins = make_change(C, denominations)
    assert sum(coins.values()) == 2
    print_solution(coins)

    C = 25
    print("Change: {}".format(C))
    print("Denominations: {}".format(denominations))
    coins = make_change(C, denominations)
    assert sum(coins.values()) == 3
    print_solution(coins)


if __name__ == '__main__':
    main()
