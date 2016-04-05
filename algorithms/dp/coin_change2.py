#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: coin_change2.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Determine fewest coins from a given set of denominations
needed to provide change for an amount "money" using recursion.

This only works for Python >= 3.2 as it makes use of functools.lru_cache for memoization
"""

from functools import lru_cache

@lru_cache(maxsize=None)
def recursive_change(money, denominations):
    # print("Finding change for {}".format(money))

    if money == 0:
        return 0, ()

    coins_used = None
    min_coins_used = float('inf')
    for coin in denominations:
        if money >= coin:
            num_coins_used, coins = recursive_change(money - coin,
                                                     denominations)
            if num_coins_used + 1 < min_coins_used:
                coins_used = coins + (coin,)  # Concatenate tuples
                min_coins_used = num_coins_used + 1

    return min_coins_used, coins_used


from collections import Counter

def make_change(money, denominations):
    min_coins_used, coins_used = recursive_change(money, denominations)
    return Counter(coins_used)


def print_solution(coins):
    """coins is a Counter/dict object with denominations as keys
    and the number of coins for each denomination as values."""
    print("Minimum number of coins required: {}".format(
        sum(coins.values())))
    for value, count in coins.items():
        print("{} x {}".format(count, value))

    print('-' * 40)


def main():
    denominations = (1, 2, 4, 5, 10)

    C = 40
    print("Change: {}".format(C))
    print("Denominations: {}".format(denominations))
    coins = make_change(C, denominations)
    # assert sum(coins.values()) == 4
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

    C = 7
    print("Change: {}".format(C))
    print("Denominations: {}".format(denominations))
    coins = make_change(C, denominations)
    # assert sum(coins.values()) == 2
    print_solution(coins)

    # C = 12
    # print("Change: {}".format(C))
    # print("Denominations: {}".format(denominations))
    # coins = make_change(C, denominations)
    # assert sum(coins.values()) == 2
    # print_solution(coins)

    # C = 25
    # print("Change: {}".format(C))
    # print("Denominations: {}".format(denominations))
    # coins = make_change(C, denominations)
    # assert sum(coins.values()) == 3
    # print_solution(coins)


if __name__ == '__main__':
    main()
