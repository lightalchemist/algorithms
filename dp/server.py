#!/usr/bin/env python


"""
File: server.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Solution to chap 6 ex 12 of Algorithm Design book
by Jon Kleinberg and Eva Tardos.
"""


import numpy as np
import pdb


def build_table(p_costs):
    """p_costs[i-1] is cost to place file at ith server.
    A[i][j] = Minimum total cost considering first i servers and last file is
    placed at server j."""
    n = len(p_costs)
    A = np.zeros((n+1, n+1))
    A[0, :] = p_costs[n-1]
    place_at = [None] * (n+1)  # Create an extra dummy slot for convenient indexing
    for i in range(1, n):  # Consider server 1 to i
        # Total cost if we place a copy at server i = placement cost p_costs[i-1] + total cost
        # if we consider just up to server (i-1) with a copy of the file placed at
        # server i.
        A[i][i] = p_costs[i-1] + A[i-1][i]
        # pdb.set_trace()
        for j in range(i+1, n+1):
            A[i][j] = min(A[i][i],
                          (j-i + A[i-1][j]))

    A[n][n] = A[n-1][n]
    # A[n][n] = p_costs[n-1] + A[n-1][n]  # Server n always has a copy.
    # place_at[n] = n
    # place_at = place_at[1:]  # Exclude dummy slot.
    return A, place_at


def compute_solution(p_costs):
    n = len(p_costs)
    A, place_at = build_table(p_costs)
    total_cost = A[n][n]  # Total cost if we cosider all n servers with last copy at n.
    solution = assemble(place_at)
    # print("Place at: {}".format(place_at))
    print("A: ")
    print(A)
    return total_cost, solution


def assemble(place_at):
    """A 'Y' at position (i-1) indicates to place a copy at server i
    else a 'N' will be in that position."""
    solution = ["Y" if i == x else "N" for i, x in enumerate(place_at, 1)]
    return solution


def main():
    # p_costs = [3, 1]
    # total_cost, solution = compute_solution(p_costs)
    # assert total_cost == 2
    # print("Placement costs: {}".format(p_costs))
    # print("Total cost: {}".format(total_cost))
    # print(solution)

    # p_costs = [1, 3]
    # total_cost, solution = compute_solution(p_costs)
    # assert total_cost == 4
    # print("Placement costs: {}".format(p_costs))
    # print("Total cost: {}".format(total_cost))
    # print(solution)

    # p_costs = [1, 2, 3]
    # total_cost, solution = compute_solution(p_costs)
    # assert total_cost == 5
    # print("Placement costs: {}".format(p_costs))
    # print("Total cost: {}".format(total_cost))
    # print(solution)

    p_costs = [3, 2, 3]
    total_cost, solution = compute_solution(p_costs)
    assert total_cost == 6
    print("Placement costs: {}".format(p_costs))
    print("Total cost: {}".format(total_cost))
    print(solution)

    print("All tests pass")


if __name__ == '__main__':
    main()
