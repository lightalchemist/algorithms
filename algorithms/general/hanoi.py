#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: hanoi.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Recursive solution to Tower of Hanoi problem.
"""


def solve(num_discs, src, dst, hold):
    if num_discs == 1:
        print("{} -> {}".format(src, dst))
    else:
        solve(num_discs - 1, src, hold, dst)
        print("{} -> {}".format(src, dst))
        solve(num_discs - 1, hold, dst, src)


def test():
    solve(3, 'A', 'B', 'C')


if __name__ == '__main__':
    test()
