
"""
File: project.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Excercise 2 of Kleinberg and Tardos's dynamic
programming chapter.
"""

import numpy as np


LOW = 0
HIGH = 1
def compute_value_table(vl, vh):
    """Return matrix of profit.
    A[i][LOW]/A[i][HIGH] contains max profit for week i, i in [1, n]
    if a low/high stress job is performed on week i respectively.
    """
    assert len(vl) == len(vh)

    n = len(vl)
    A = np.zeros((n+1, 2))
    A[1][LOW] = vl[0]
    A[1][HIGH] = vh[0]
    for i in range(2, n+1):  # Week 2 to n
        # value of low stress job for week i  + max of low/high
        # stress job for week (i - 1)
        A[i][LOW] = vl[i-1] + max(A[i-1][LOW],
                                  A[i-1][HIGH])
        # value of high stress job for week i + max of low/high
        # stress job for week (i - 2) as we skip week (i - 1)
        A[i][HIGH] = vh[i-1] + max(A[i-2][LOW],
                                   A[i-2][HIGH])

    return A


def assemble_plan(A):
    """Backtrack to find optimal plan."""
    n = A.shape[0] - 1  # Total number of weeks
    solution = [None] * n
    while n > 0:
        if A[n][HIGH] > A[n][LOW]:
            solution[n-1] = "high"
            if n > 1:  # Skip working for prev week other than week 1
                solution[n-2] = "none"
                n -= 2
        else:
            solution[n-1] = "low"
            n -= 1

    return solution


def main():
    vl = [10, 1, 10, 10]
    vh = [5, 50, 5, 1]
    A = compute_value_table(vl, vh)
    print("Value table:")
    print(A)
    print("Value of optimal plan: {}".format(np.max(A[-1, :])))

    solution = assemble_plan(A)
    print("Plan: {}".format(solution))

if __name__ == '__main__':
    main()
