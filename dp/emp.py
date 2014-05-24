#!/usr/bin/env python


import numpy as np


def build_table(x, f):
    n = len(x) + 1
    A = np.zeros(n)
    A[1] = min(x[0], f[0])
    save_from = [None] * n
    # save_from = [-1] * n
    for i in range(2, n):
        # activate at time i
        # Max monster we can kill at time i is
        # max of max monster we can kill at time j, A[j],
        # + monsters we can kill at time i after saving up
        # emp from time j
        possible_kills = [min(x[i-1],  # Monster at time i
                              f[i-1-j])  # Num that can be killed saving from j
                          + A[j]  #  Max num that can be killed at time j
                          for j in range(i)]  # saving from time 0 to i - 1
        idx = np.argmax(possible_kills)  # Time to start saving emp from.
        max_kills_at_i = possible_kills[idx]
        save_from[i] = idx  # To achieve max kills at time i, start save from idx

        A[i] = max(A[i-1],  # Don't activate at time i, max kill as 1 step earlier
                   max_kills_at_i) # activate at time i.

    return A, save_from


def assemble(x, f, A, save_from):
    i = len(x)
    solution = [None] * (len(x) + 1)
    while i > 0:
        if A[i] > A[i-1]:  # activated at time i
            # print("Time {} activate".format(i))
            solution[i] = "Activate"
            # Save up from save_from[i]
            if save_from[i] is not None:
                # print("Saved from time {}".format(save_from[i]))
                solution[save_from[i]:i] = ["Don't activate"] * (i - save_from[i])
            # else:
                # print("Begin from drained.")
            i = save_from[i]
        else:
            solution[i] = "Don't activate"
            i -= 1

    return solution[1:]


def print_solution(solution):
    print("")
    print("Solution")
    for i, x in enumerate(solution, 1):
        print("Time {}: {}".format(i, x))


def main():
    x = [2]
    f = [3]
    x = [1, 10, 10, 1]
    f = [1, 2, 4, 8]
    # x = [2, 2, 7]
    # f = [2, 5, 6]
    x = [3, 10, 4, 8, 20, 10]
    f = [1, 4, 6, 8, 10, 15]
    A, save_from = build_table(x, f)
    print("A: {}".format(A))
    # print("save_from: {}".format(save_from))

    print("x: {}".format(x))
    print("f: {}".format(f))
    solution = assemble(x, f, A, save_from)
    print_solution(solution)
    print("Total destroyed: {}".format(A[-1]))


if __name__ == '__main__':
    main()
