
"""
File: weighted_interval_scheduling.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description:
    DP solution to weighted interval scheduling problem.
    Solution mirrors pseudocode given in the book
    Algorithm Design by Jon Kleinberg and Eva Tardos.
"""


import numpy as np


# def binary_search(jobs, start, low, high):
#     mid = (high + low) // 2
#     if mid <= 1 and jobs[mid][1] > start:
#         return 0
#     elif
#
#     if jobs[mid][1] > start:  # Not found
#         return 0


def print_schedule(jobs):
    for start, end in jobs:
        print(' '*(start+3) + '({})'.format(start) + '|' +
              '-'*(end - start - 1) + '|' + "({})".format(end))
        print("")


def search(jobs, start, i):
    while i >= 0:
        if jobs[i][1] < start:
            return i
        else:
            i -= 1

    return -1


def compute_p(jobs):
    """Computes index of latest finished job that does not overlap with a job."""
    n = len(jobs)
    p = np.zeros(n, dtype=np.uint)
    for i in range(n):
        start_i = jobs[i][0]
        # Start searching from previous job.
        # Add 1 so that p[0] == 0, and index matches index of table A.
        p[i] = search(jobs, start_i, i-1) + 1

    return p


def compute_WIS_table(jobs, values):
    """jobs = [(start_1, end_1), ..., (start_n, end_n)]
    A[i] stores the max value of soln after considering ith job.
    i ranges from 0 to n, with i == 0 as "dummy" cell.
    Total time complexity: O(n^2) because of compute_p(). compute_p() can be
    made faster by using binary_search or using another list of jobs sorted
    according to start time.
    """
    jobs = sorted(jobs, key=lambda x: x[1])  # Sort according to finishing time.
    p = compute_p(jobs)

    n = len(jobs)
    A = np.zeros(n+1)
    for i in range(1, n+1):
        # Max between having ith job in solution and without ith job.
        # p[i-1] is index of latest job whose finishing time did not overlap with ith job
        # Include ith job: values[i-1] + A[p[i-1]]
        # Exclude ith job: A[i-1]
        A[i] = max(values[i-1] + A[p[i-1]], A[i-1])

    return A


def solve(jobs, values, A):
    solution = []
    n = len(A) - 1
    while n > 0:
        if A[n] - values[n-1] >= A[n-1]:
            solution.append(jobs[n-1])

        n -= 1

    return solution


def main():
    jobs = [(1, 3), (2, 4), (5, 7)]
    values = [1, 2, 3]
    jobs = sorted(jobs, key=lambda x: x[1])  # Sort according to finishing time.
    print('-' * 20)
    print("Schedule:")
    print_schedule(jobs)

    # p = compute_p(jobs)
    # print("")
    # print(p)
    A = compute_WIS_table(jobs, values)
    print('-' * 20)
    print("Table:")
    print(A)
    print('-' * 20)
    solution = solve(jobs, values, A)
    print("Solution: ")
    print(solution)


if __name__ == '__main__':
    main()
