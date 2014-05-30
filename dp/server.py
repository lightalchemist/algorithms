#!/usr/bin/env python


import numpy as np


def build_table(p_costs):
    """p_costs[i-1] is cost to place file at ith server.
    A[i][j] = Minimum total cost considering first i servers and last file is
    placed at server j."""
    n = len(p_costs)
    A = np.zeros((n + 1, n+1))
    place_at = [None] * (n+1)
    for i in range(1, n):  # Total cost if we consider up to server i
        # Cost to place a copy at i = placement cost p_costs[i-1] + total cost
        # if we consider up to server (i-1) with a copy of the file placed at
        # server i.
        ci = p_costs[i-1] + A[i-1][i]
        possible = [(ci, i)] + [(j - i + A[i-1][j], j) for j in range(i+1, n+1)]
        # for j in range(i+1, n+1):  # Next closest file could be at anywhere from server (i+1) to server n.
        #     # Minimum total cost if we consider server 1 to i
        #     A[i][j] = min(ci,
        #                   (j - i) + A[i-1][j]) # Search cost + total cost considering first i-1 servers

        A[i][j], place_at[i] = min(possible)


    A[n][n] = p_costs[n-1] + A[n-1][n]  # Server n always has a copy.
    return A, place_at


def compute_cost(p_costs):
    n = len(p_costs)
    A, place_at = build_table(p_costs)
    return A[n][n]


def main():
    p_costs = [3, 1]
    # A = build_table(p_costs)
    # print(A)
    total_costs = compute_cost(p_costs)
    assert total_costs == 2

    p_costs = [1, 3]
    total_costs = compute_cost(p_costs)
    assert total_costs == 4

    p_costs = [1, 2, 3]
    total_costs = compute_cost(p_costs)
    assert total_costs == 5

    print("All tests pass")


if __name__ == '__main__':
    main()
