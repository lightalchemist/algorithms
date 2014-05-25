#!/usr/bin/env python

import numpy as np


def build_table(values, C):
    A = np.zeros(C + 1, dtype=np.int)
    parents = np.zeros(C+1, dtype=np.int)
    for i in range(1, C+1):
        A[i] = min(1 + A[i- v] for v in values if i >= v)

    return A


def assemble(values, C, A):
    pass

def main():
    values = [1, 2, 5, 10]
    C = 2
    A = build_table(values, C)
    print(A)


if __name__ == '__main__':
    main()
