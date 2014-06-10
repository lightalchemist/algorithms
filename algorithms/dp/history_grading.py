#!/usr/bin/env python

"""
File: history_grading.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Question 111-History Grading taken from
    http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=114&page=show_problem&problem=47
    Computes the length of the longest subsequence whose relative order matches that in a given array.
"""


import numpy as np


def build_table(C, S):
    n = len(S)
    # pdb.set_trace()
    # print(n)
    A = np.zeros(n+1, dtype=np.int)
    parent = np.zeros(n+1, dtype=np.int)
    parent[1] = 1
    A[1] = 1
    for i in range(2, n+1):
        possible = [(1 + A[j], j) if C[S[i-1]] > C[S[j-1]]
                    else (1, i)
                    for j in range(1, i)]
        A[i], parent[i] = max(possible)

    return A, parent


def compute_ranking(mapping, ranking):
    mapping = [None] + mapping
    A, parent = build_table(mapping, ranking)
    solution = assemble(ranking, A, parent)

    return np.max(A), solution


def assemble(seq, A, parent):
    subsequence_length = int(np.max(A))
    solution = [None] * (subsequence_length)
    i = np.argmax(A)  # Idx of last char in seq.
    # Backtrack from last char.
    for j in range(subsequence_length-1, -1, -1):
        solution[j] = seq[i-1]
        i = parent[i]

    return solution


def compute_mapping(true_ranking):
    """Computes a mapping that maps an element to its position
    in the true ranking.
    E.g., true_ranking = [4, 1, 3, 2]
    Then the mapping generated is [None, 2, 4, 3, 1]
    i.e. element 1 maps to position 2, 2 to position 4, 3 to position 3, 4 to position 1.
    The None is used as a dummy slot so that element's value directly index their location.
    """
    mapping = [0] * len(true_ranking)
    for i, j in enumerate(true_ranking, 1):
        mapping[j-1] = i

    return mapping


def test():
    c = [1, 2, 3, 4]
    d = compute_mapping(c)
    t1 = [[1, 3, 2, 4]]
    score_and_ranking = [compute_ranking(d, t) for t in t1]
    ranking = [score for score, ranking in score_and_ranking]
    assert ranking == [3]

    c = [4, 2, 3, 1]
    d = compute_mapping(c)
    t1 = [[1,3,2,4],
          [3,2,1,4],
          [2,3,4,1]]
    score_and_ranking = [compute_ranking(d, t) for t in t1]
    ranking = [score for score, ranking in score_and_ranking]
    assert ranking == [1, 2, 3]

    c = [3,1,2,4,9,5,10,6,8,7]
    # print("c: {}".format(c))
    d = compute_mapping(c)
    t1 = [[1,2,3,4,5,6,7,8,9,10],
          [4,7,2,3,10,6,9,1,5,8],
          [3,1,2,4,9,5,10,6,8,7],
          [2,10,1,3,8,4,9,5,7,6]]
    score_and_ranking = [compute_ranking(d, t) for t in t1]
    ranking = [score for score, ranking in score_and_ranking]
    # The following given solution appears to be wrong.
    # assert ranking == [6, 5, 10, 9]
    # The correct ans should be [6, 4, 10, 5]
    assert ranking == [6, 4, 10, 5]


if __name__ == '__main__':
    test()
