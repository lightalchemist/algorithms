#!/usr/bin/env python


"""
File: server.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Solution to chap 6 ex 12 of Algorithm Design book
by Jon Kleinberg and Eva Tardos.

There are n servers s1, ..., sn.

Placing a file at server i cost a value of ci.

If a file is requested from si and the file is not found, then a search
will have to be performed from servers s_i+1 onwards. If the file is then
found at server j, where j > i, then the search cost is (j-i).

sn always has a copy of the file.

Find the optimimum strategy, i.e., whether to place a file at any of the servers,
so as to minimize the total placement and search costs.

"""


import numpy as np


def build_table(p_costs):
    """p_costs[i-1] is cost to place file at ith server.
    A[i][j] = Minimum total cost considering first i servers and last file is
    placed at server j including cost to always have a copy at server n."""
    n = len(p_costs)
    A = np.zeros((n+1, n+1))
    A[0, :] = p_costs[n-1]  # We always incur a cost to place file at server n.
    place_at = [None] * (n + 1)  # place_at[i] = 'Y' if place a copy at server i
    for i in range(1, n):  # Total cost if we only consider server 1 up to i + fixed cost for server n
        # Total cost if we place a copy at server i = placement cost p_costs[i-1] + total cost
        # if we consider just up to server (i-1) with a copy of the file placed at
        # server i.
        A[i][i] = p_costs[i-1] + A[i-1][i]
        for j in range(i+1, n+1):
            if A[i][i] < (j-i + A[i-1][j]): # Cheaper to place at copy at server i than to do search
                # By not using <=, we prefer search to placing a copy if cost is same.
                A[i][j] = A[i][i]
                place_at[i] = 'Y'
            else:
                A[i][j] = (j-i + A[i-1][j])  # Search at subsequent servers incurring search cost of (j-i).
                place_at[i] = 'N'

    # Cost is same as total cost if only first (n-1) servers are considered as placement cost of server n
    # is already included previously
    A[n][n] = A[n-1][n]
    place_at[n] = 'Y'  # We always place a copy at n as required by the question.
    return A, place_at[1:]


def compute_solution(p_costs):
    n = len(p_costs)
    A, solution = build_table(p_costs)
    total_cost = A[n][n]  # Total cost if we cosider all n servers with last copy at n.
    return total_cost, solution


def main():
    p_costs = [1]
    total_cost, solution = compute_solution(p_costs)
    assert total_cost == 1
    assert solution == ['Y']
    print("Placement costs: {}".format(p_costs))
    print("Total cost: {}".format(total_cost))
    print(solution)
    print("")

    p_costs = [3, 1]
    total_cost, solution = compute_solution(p_costs)
    assert total_cost == 2
    assert solution == ['N', 'Y']
    print("Placement costs: {}".format(p_costs))
    print("Total cost: {}".format(total_cost))
    print(solution)
    print("")

    p_costs = [1, 3]
    total_cost, solution = compute_solution(p_costs)
    assert total_cost == 4
    assert solution == ['N', 'Y']
    print("Placement costs: {}".format(p_costs))
    print("Total cost: {}".format(total_cost))
    print(solution)
    print("")

    p_costs = [1, 2, 3]
    total_cost, solution = compute_solution(p_costs)
    assert total_cost == 5
    assert solution == ['Y', 'N', 'Y']
    print("Placement costs: {}".format(p_costs))
    print("Total cost: {}".format(total_cost))
    print(solution)
    print("")

    p_costs = [3, 2, 3]
    total_cost, solution = compute_solution(p_costs)
    assert total_cost == 6
    assert solution == ['N', 'N', 'Y']
    print("Placement costs: {}".format(p_costs))
    print("Total cost: {}".format(total_cost))
    print(solution)
    print("")

    p_costs = [1, 3, 2, 1]
    total_cost, solution = compute_solution(p_costs)
    assert total_cost == 1 + 2 + 1 + 1
    assert solution == ['Y', 'N', 'N', 'Y']
    print("Placement costs: {}".format(p_costs))
    print("Total cost: {}".format(total_cost))
    print(solution)
    print("")

    p_costs = [1, 3, 4, 1]
    total_cost, solution = compute_solution(p_costs)
    assert total_cost == 1 + 2 + 1 + 1
    assert solution == ['Y', 'N', 'N', 'Y']
    print("Placement costs: {}".format(p_costs))
    print("Total cost: {}".format(total_cost))
    print(solution)
    print("")

    print("All tests pass")


if __name__ == '__main__':
    main()
