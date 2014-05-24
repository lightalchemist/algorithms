#!/usr/bin/env python

"""
File: line_formatting.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Solution to chap 6 ex 6 of Algorithm Design book
by Jon Kleinberg and Eva Tardos.

This code uses DP to format a paragraph of text to ensure that
the lines are split such that each line has characters less than a given
number max_char_per_line and overall the lines are as close to
max_char_per_line as possible.
"""

import numpy as np


LARGE_NUM = np.inf
def compute_lcost(words, wl, max_char_per_line):
    """lcost[i][j] is cost of having word i to word j (inclusive) in
    a single line.
    TODO: Speed this up.
    """
    n = len(words) + 1
    lcost = np.zeros((n, n))
    for i in range(1, n):
        for j in range(i, n):
            num_chars = sum(wl[i-1:j]) + (j - i)
            lcost[i][j] = ((num_chars - max_char_per_line)**2  # Penalty
                           if num_chars <= max_char_per_line  # if satisfy constraint.
                           else LARGE_NUM)  # Disallow constraint to be violated.

    return lcost


def compute_lcost2(words, wl, max_char_per_line):
    n = len(words) + 1
    lcost = np.ones((n, n)) * -1
    # lcost[:, 0] = -1
    # Error cost for sentence with words wi to wj
    for i in range(1, n):
        for j in range(i, n):
            lcost[i][j] = lcost[i][j-1] + 1 + wl[j-1]

    lcost = (lcost - max_char_per_line)**2
    lcost[0, :] = 0
    lcost[:, 0] = 0
    lcost[np.tril_indices(lcost.shape[0], -1)] = 0

    return lcost


def build_table(words, max_char_per_line):
    """A[j] = optimum cost of formatting paragraph upto and including jth word.
    A[len(words)] = optimum cost to format entire paragraph of words.
    """
    wl = map(len, words)  # Word lengths
    lcost = compute_lcost(words, wl, max_char_per_line)
    A = np.zeros(len(words) + 1)
    for j in range(1, len(words) + 1):
        # Cost to format j words is opt cost to format up to
        # (i-1)th word A[i-1] + cost to have ith to jth word (lcost_ij) in a
        # single line.
        A[j] = min(A[i-1] + lcost[i][j] for i in range(1, j+1))

    return A


def assemble(words, A, lcost):
    sentences = []
    n = len(words)
    while n > 0:
        i = np.argmin(np.asarray([A[k-1] + lcost[k][n] for k in range(1, n+1)]))
        sentences.insert(0, " ".join(words[i:n]))  # Word i to word n-1 form a sentence.
        n -= (n - i)  # Less (n - i) number of words.

    return '\n'.join(sentences)


def format(paragraph, max_char_per_line):
    words = paragraph.split()
    wl = map(len, words)
    lcost = compute_lcost(words, wl, max_char_per_line)
    A = build_table(words, max_char_per_line)
    formatted = assemble(words, A, lcost)
    return formatted


# The paragraphs below are taken from the following website:
# https://www.python.org/doc/humor/#legal-issues

para1 = """
Microsoft reportedly is willing to stop the action if either a licensing
agreement can be worked out or if Guido Van Rossum, the inventer, changes the name of the
computer language and personally destroys all references to Spam, the Spanish Inquisition, and so
forth, in all copies of the Python code and documentation whereever they may have propagated.
"""

para2 = '''
A highly placed White House Official claims that President Clinton takes the
matter very seriously and is willing to break off all diplomatic relations with
the government of Japan over the issue. "We're beginning to wonder if this
information super-highway thing is such a good idea after all," she said. The
ambassador of Japan in Washington is reportedly "very, very confused."
'''

def test():
    words = para1.split()
    max_char_per_line = 79
    wl = map(len, words)
    lcost = compute_lcost(words, wl, max_char_per_line)
    A = build_table(words, max_char_per_line)
    formatted = assemble(words, A, lcost)
    print(formatted)


def main():
    test()


if __name__ == '__main__':
    main()
