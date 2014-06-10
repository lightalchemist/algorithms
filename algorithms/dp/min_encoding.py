#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: min_encoding.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Given a string and a list of codewords,
find the encoding that requires the
minimum number of codewords to represent the string.

E.g., codewords = ["a", "ba", "abab", "b"]
string s = "bababbaababa"
Desired output is ("b", "abab", "ba", "abab", "a")

Problem taken from Algorithm Design Manual by Steven Skiena 1st Ed.
Qn 3-9 pg 79.
"""

import numpy as np


def build_table(text, codebook):
    A = np.empty(len(text) + 1)
    A.fill(np.inf)
    A[0] = 0  # 0 cost to encode empty string.
    words_used = [None] * (len(text) + 1)
    for i in range(1, len(text) + 1):
        possible = [(1 + A[i - len(w)], w)
                    if text[:i].endswith(w)
                    else (np.inf, "")
                    for w in codebook]

        A[i], words_used[i] = min(possible)

    return A, words_used


def assemble(text, words_used):
    n = len(text)
    result = []
    while n > 0:
        result.append(words_used[n])
        n -= len(words_used[n])

    return list(reversed(result))


def encode(text, codebook):
    if not text:  # Empty string
        return []

    A, words_used = build_table(text, codebook)
    # pdb.set_trace()
    if A[-1] == np.inf:
        return []  # No possible encoding
    encoding = assemble(text, words_used)
    return encoding


def min_encode_length(text, codebook):
    if not text:
        return 0

    min_count = len(text)
    for word in codebook:
        if text.endswith(word):
            count = 1 + min_encode_length(text[:len(text) - len(word)], codebook)
            if count < min_count:
                min_count = count

    return min_count


def test():
    codewords = ["a", "ba", "abab", "b"]
    s = ""
    encoding = encode(s, codewords)
    assert len(encoding) == 0
    assert "".join(encoding) == s

    codewords = ["a", "ba", "abab", "b"]
    s = "bababbaababa"
    encoding = encode(s, codewords)
    assert len(encoding) == 5
    assert "".join(encoding) == s

    codewords = ["a", "ba", "abab", "b"]
    s = "ababcba"
    encoding = encode(s, codewords)
    assert len(encoding) == 0
    assert "".join(encoding) == ""

    codewords = ["a", "c"]
    s = "cccc"
    encoding = encode(s, codewords)
    assert len(encoding) == 4
    assert "".join(encoding) == s

    codewords = ["abc"]
    s = "abc"
    encoding = encode(s, codewords)
    assert len(encoding) == 1
    assert "".join(encoding) == s

    codewords = ["a", "abc", "bc", "ac"]
    s = "abc"
    encoding = encode(s, codewords)
    assert len(encoding) == 1
    encoding == ["abc"]
    assert "".join(encoding) == s

    codewords = ["a", "abc", "bc", "ac", "ab"]
    s = "abc"
    encoding = encode(s, codewords)
    assert len(encoding) == 1
    encoding == ["abc"]
    assert "".join(encoding) == s

    codewords = ["a", "bc", "ac", "ab"]
    s = "abc"
    encoding = encode(s, codewords)
    assert len(encoding) == 2
    encoding == ["a", "bc"]
    assert "".join(encoding) == s

    codewords = ["a", "cc", "bc", "ac", "ab"]
    s = "abccab"
    encoding = encode(s, codewords)
    assert len(encoding) == 3
    encoding == ["ab", "cc", "ab"]
    assert "".join(encoding) == s


if __name__ == '__main__':
    test()
