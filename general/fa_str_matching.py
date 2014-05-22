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


import sys
from collections import defaultdict


def build_next_state_table(pattern, charset):
    m = len(pattern)
    next_state = [defaultdict(int) for _ in range(m + 1)]

    prefix = ''
    for k, c in enumerate(pattern):
        for a in charset:
            pass
            next_state[k+1]

    return next_state


def match(pattern, text, next_state=None):
    if next_state is None:
        charset = set(text.split())
        next_state = build_next_state_table(pattern, charset)

    pattern_length = len(pattern)
    state = 0
    for i, token in enumerate(text, 1):
        state = next_state[state][token]
        if state == pattern_length:  # Reached end of pattern, i.e., match found.
            yield i - pattern_length  # Number of chars from beginning of text.


def print_matches(pattern, text, matcher):
    pattern_length = len(pattern)
    print('-' * max(pattern_length, 50))
    print("Search pattern : {}".format(pattern))
    print('-' * max(pattern_length, 50))
    for num_shifts in matcher:
        print(text)
        print(' '*num_shifts + '^'*pattern_length)


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


def print_usage():
    print("Given a pattern and text, find all occurrences of the pattern in the text.")
    print("Usage: {} <pattern> <text>".format(sys.argv[0]))


def main():
    if len(sys.argv) < 3:
        print_usage()
        return

    pattern, text = sys.argv[1:3]
    print_matches(pattern, text, match(pattern, text))


if __name__ == '__main__':
    main()
