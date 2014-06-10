#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: min_steps_to_one.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description:
http://www.codechef.com/wiki/tutorial-dynamic-programming#Problem_:_Minimum_Steps_to_One

Problem Statement:
On a positive integer, you can perform any one of the following 3 steps.
1.) Subtract 1 from it. ( n = n - 1 )  ,
2.) If its divisible by 2, divide by 2. ( if n % 2 == 0 , then n = n / 2  ),
3.) If its divisible by 3, divide by 3. ( if n % 3 == 0 , then n = n / 3  ).
Now the question is, given a positive integer n,
find the minimum number of steps that takes n to 1
eg:
1.)For n = 1 , output: 0
2.) For n = 4 , output: 2  ( 4  /2 = 2  /2 = 1 )
3.)  For n = 7 , output: 3  (  7  -1 = 6   /3 = 2   /2 = 1 )

"""

import numpy as np


def compute_table(n):
    A = np.zeros(n + 1, dtype=np.uint)
    step = [None] * (n + 1)
    for i in range(2, n+1):
        possible = [(1 + A[i-1], "-1"),
                    (1 + A[i//2] if i % 2 == 0 else np.inf, "/2"),
                    (1 + A[i//3] if i % 3 == 0 else np.inf, "/3")]
        A[i], step[i] = min(possible)

    return A, step


def assemble_solution(n, step):
    solution = []
    while n > 1:
        # solution.append(step[n])
        if step[n] == "-1":
            result = "{} - 1 = {}".format(n, n-1)
            n -= 1
        elif step[n] == "/2":
            result = "{} / 2 = {}".format(n, n/2)
            n /= 2
        elif step[n] == "/3":
            result = "{} / 3 = {}".format(n, n/3)
            n /= 3
        else:
            raise ValueError

        solution.append(result)

    solution.append("Reached n = 1")
    return solution


def compute_num_steps(n):
    A, step = compute_table(n)
    # print(A)
    solution = assemble_solution(n, step)
    return A[n], solution


def main():
    n = 1
    num_steps, solution = compute_num_steps(n)
    print("n: {}".format(n))
    print(solution)
    assert num_steps == 0

    n = 4
    num_steps, solution = compute_num_steps(n)
    print("n: {}".format(n))
    print(solution)
    assert num_steps == 2

    n = 7
    num_steps, solution = compute_num_steps(n)
    print("n: {}".format(n))
    print(solution)
    assert num_steps == 3

    print("All test pass.")


if __name__ == '__main__':
    main()
