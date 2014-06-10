#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: base_conversion.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Code to convert string representation of a number in base b1 to
string representation of that number in base b2.

Problem 5.7 of Elements of Programming Interview (pg. 49).
"""

import string


def build_mapping():
    chars = list(string.digits) + ["A", "B", "C", "D", "E", "F"]
    char2int = dict(zip(chars, range(17)))
    int2char = dict(zip(range(17), chars))
    return char2int, int2char


def convert(s, b1, b2):
    """Convert string representation of a number in base b1
    to string representation of the number in base b2.
    s: String representation of number to convert
    b1: Integer base of s.
    b2: Base to convert to.
    2 <= b1, b2 <= 16
    """
    char2int, int2char = build_mapping()
    number = 0
    neg = False
    start = 0

    if s[0] == '-':
        neg = True
        start = 1

    # Convert to base 10
    for i in range(start, len(s)):
        try:
            number *= b1
            number += char2int[s[i]]
        except KeyError:
            raise ValueError("String input contains invalid char {}"
                                " that cannot be converted to int.".format(s[i]))

    # Convert to base b2
    result = []
    while number:
        remainder = number % b2
        result.append(int2char[remainder])
        number /= b2

    # Handle negative sign.
    if result:
        if neg:
            result.append('-')
    else:
        result.append("0")

    return "".join(reversed(result))


def convert2(s, b1, b2):
    """Convert string representation of a number in base b1
    to string representation of the number in base b2.
    s: String representation of number to convert
    b1: Integer base of s.
    b2: Base to convert to.
    2 <= b1, b2 <= 16
    """
    char2int, int2char = build_mapping()
    number = 0
    neg = False

    # Convert to base 10
    for power, i in enumerate(range(len(s) - 1, -1, -1)):
        try:
            number += char2int[s[i]] * (b1**power)
        except KeyError:
            if s[i] == '-' and i == 0:
                neg = True
            else:
                raise ValueError("String input contains invalid char {}"
                                 " that cannot be converted to int.".format(s[i]))

    # Convert to base b2
    result = []
    while number:
        remainder = number % b2
        result.append(int2char[remainder])
        number /= b2

    if result:
        if neg:
            result.append('-')
    else:
        result.append("0")

    return "".join(reversed(result))


def test():
    s = "1"
    result = convert(s, 10, 10)
    assert result == "1"

    s = "A"
    result = convert(s, 16, 2)
    assert result == "1010"

    s = "C"
    result = convert(s, 16, 10)
    assert result == "12"

    s = "0"
    result = convert(s, 3, 4)
    assert result == "0"

    s = "-F"
    result = convert(s, 16, 10)
    assert result == "-15"

    s = "FF"
    result = convert(s, 16, 8)
    assert result == "377"

    s = "1A"
    result = convert(s, 16, 10)
    assert result == "26"

    s = "FF"
    result = convert(s, 16, 2)
    assert result == "11111111"

    s = "1001"
    result = convert(s, 2, 16)
    assert result == "9"

    s = "237"
    result = convert(s, 9, 8)
    assert result == "304"


if __name__ == '__main__':
    test()
