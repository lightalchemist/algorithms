#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: excel_id2int.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Convert Excel-like column string label to integer.
E.g., "A" -> 1, "B" -> 2, ..., "Z" -> 26
"AZ" -> 1*27 + 26, "ZCE" -> 26*27**2 + 3*27 + 5

Problem 5.8 of Elements of Programming Interview (pg. 49).
"""


import string


# Mapping from uppercase char to int
mapping = {c:i for i, c in enumerate(string.uppercase, 1)}
def convert(s):
    s_orig = s
    s = s.upper()
    result = 0
    base = 1
    for i in range(len(s)-1, -1, -1):
        try:
            result += mapping[s[i]] * base
            base *= 27
        except KeyError:
            raise ValueError("Non-alphabet character {}"
                             " found in given string {}".format(s[i], s_orig))

    return result


def test():
    s = "A"
    result = convert(s)
    assert result == 1

    s = "Z"
    result = convert(s)
    assert result == 26

    s = "AZ"
    result = convert(s)
    assert result == (27 + 26)

    s = "XYZ"
    result = convert(s)
    assert result == (24*27**2 + 25*27 + 26)


if __name__ == '__main__':
    test()
