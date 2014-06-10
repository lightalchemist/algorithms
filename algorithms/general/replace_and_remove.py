#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
File: replace_and_remove.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Given a string S, replace all 'a' with "aa" and delete all 'b's.
Time complexity: O(n)
Space complexity: O(1)
Assume S can be resized to fit the new string.

This question and solution is from Elements of Programming Interview
question 6-21.

"""


def replace_and_remove(S):
    S = list(S)  # Make S writable as Pyton str is immutable.

    write_idx = 0
    a_counts = 0
    for c in S:
        if c == 'a':
            a_counts += 1

        if c != 'b':
            S[write_idx] = c  # Copy chars into position except 'b'.
            write_idx += 1

    # At this stage, write_idx is 1 pass last char of seq
    # with 'b' deleted
    # Total size of modified S is write_idx + a_counts
    if write_idx + a_counts > len(S):
        S += [None] * (write_idx + a_counts - len(S))
    else:
        S = S[:write_idx + a_counts]

    cur_idx = write_idx - 1  # Idx pointing to part of original S to copy from.
    write_idx = len(S) - 1  # Idx in S to write to.
    while write_idx >= 0:
        if S[cur_idx] == 'a':  # Write 2 'a's.
            S[write_idx] = 'a'
            S[write_idx - 1] = 'a'
            write_idx -= 2
        elif S[cur_idx] != 'b':  # Just copy the char over.
            S[write_idx] = S[cur_idx]
            write_idx -= 1

        cur_idx -= 1

    return "".join(S)


def test():
    S = "abcadef"
    S_new = replace_and_remove(S)
    assert S_new == "aacaadef"

    S = "abbcbadefba"
    S_new = replace_and_remove(S)
    assert S_new == "aacaadefaa"

    S = "b"
    S_new = replace_and_remove(S)
    assert S_new == ""

    S = "a"
    S_new = replace_and_remove(S)
    assert S_new == "aa"

    S = "c"
    S_new = replace_and_remove(S)
    assert S_new == "c"

    S = "cde"
    S_new = replace_and_remove(S)
    assert S_new == "cde"

    S = "cdea"
    S_new = replace_and_remove(S)
    assert S_new == "cdeaa"

    S = "cbe"
    S_new = replace_and_remove(S)
    assert S_new == "ce"


if __name__ == '__main__':
    test()
