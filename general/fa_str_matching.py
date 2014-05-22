#!/usr/bin/env python

"""
File: fa_str_matching.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: String matching using finite automata.
Implementation follows closely the pseudocode given in the book
Algorithms Unlocked by Thomas H. Cormen.
"""


def build_next_state_table(pattern, charset):
    pass


def match(pattern, text, next_state=None):
    if next_state is None:
        charset = set(text.split())
        next_state = build_next_state_table(pattern, charset)

    m = len(pattern)
    state = 0
    for i, c in enumerate(text, 1):
        state = next_state[state][c]
        if state == m:
            yield i - m


from collections import defaultdict


def print_matches(pattern, text, matcher):
    m = len(pattern)
    print('-' * max(m, 50))
    print("Search pattern : {}".format(pattern))
    print('-' * max(m, 50))
    for i in matcher:
        print(text)
        print(' '*i + '^'*m)


def test():
    pattern = "ACACAGA"
    m = len(pattern)
    next_state = [defaultdict(int) for _ in range(m + 1)]
    next_state[0]['A'] = 1

    next_state[1]['A'] = 1
    next_state[1]['C'] = 2

    next_state[2]['A'] = 3

    next_state[3]['A'] = 1
    next_state[3]['C'] = 4

    next_state[4]['A'] = 5

    next_state[5]['A'] = 1
    next_state[5]['C'] = 4
    next_state[5]['G'] = 6

    next_state[6]['A'] = 7

    next_state[7]['A'] = 1
    next_state[7]['C'] = 2

    text = "GTAACACAGAACACAGACGA"
    print_matches(pattern, text, match(pattern, text, next_state))


import sys
def print_usage():
    print("{} <pattern> <text>".format(sys.argv[0]))


def main():
    if len(sys.args) < 3:
        print_usage()

    pattern, text = sys.argv[1:3]
    print_matches(pattern, text, match(pattern, text))


if __name__ == '__main__':
    main()
