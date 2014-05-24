#!/usr/bin/env python


import numpy as np


LARGE_NUM = 1000000
def compute_lcost(words, wl, L):
    n = len(words) + 1
    lcost = np.zeros((n, n))

    for i in range(1, n):
        for j in range(i, n):
            e = sum(wl[i-1:j]) + (j - i)
            if e <= L:
                lcost[i][j] = (e - L)**2
            else:
                lcost[i][j] = LARGE_NUM
            # lcost[i][j] = (e - L)**2 if e <= L else LARGE_NUM

    return lcost


def compute_lcost2(words, wl, L):
    n = len(words) + 1
    lcost = np.ones((n, n)) * -1
    # lcost[:, 0] = -1
    # Error cost for sentence with words wi to wj
    for i in range(1, n):
        for j in range(i, n):
            lcost[i][j] = lcost[i][j-1] + 1 + wl[j-1]

    lcost = (lcost - L)**2
    lcost[0, :] = 0
    lcost[:, 0] = 0
    lcost[np.tril_indices(lcost.shape[0], -1)] = 0

    return lcost


def build_table(words, L):
    wl = map(len, words)  # Word lengths
    lcost = compute_lcost(words, wl, L)
    A = np.zeros(len(words) + 1)
    for j in range(1, len(words) + 1):
        # A[j] = min(A[i-1] + 1 + lcost[i][j] for i in range(1, j+1))
        A[j] = min(A[i-1] + lcost[i][j] for i in range(1, j+1))

    return A


import pdb
def assemble(words, A, lcost):
    sentences = []
    n = len(words)
    while n > 0:
        i = np.argmin(np.asarray([A[k-1] + lcost[k][n] for k in range(1, n+1)]))
        sentences.insert(0, " ".join(words[i:n]))
        n -= (n - i)

    return '\n'.join(sentences)


def format(paragraph, L):
    words = paragraph.split()
    wl = map(len, words)
    lcost = compute_lcost(words, wl, L)
    A = build_table(words, L)
    formatted = assemble(words, A, lcost)
    return formatted


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
    global para1
    words = para1.split()
    L = 79
    # L = 70
    wl = map(len, words)
    lcost = compute_lcost(words, wl, L)
    A = build_table(words, L)
    formatted = assemble(words, A, lcost)
    return formatted


def main():
    test()


if __name__ == '__main__':
    main()
