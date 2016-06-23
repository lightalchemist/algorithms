#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: balanced_brackets.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Check if brackets in given expression are balanced
"""


def verify_balanced_brackets(expr):
    print("Checking expression: {}".format(expr))

    # Close and open pairs
    pair = {')': '(',
            ']': '[',
            "'": "'",
            '"': '"',
            '}': '{'}

    brackets = set(pair.keys() + pair.values())

    stack = []
    for c in expr:
        if c not in brackets:  # Skip non-bracket symbols
            continue

        if not stack:
            stack.append(c)
        elif pair.get(c, None) == stack[-1]:  # Check for pair
            stack.pop()
        else:
            stack.append(c)

    return len(stack) == 0


def main():
    expr = "([])[]()"
    assert(verify_balanced_brackets(expr))

    expr = "((([()]))())"
    assert(verify_balanced_brackets(expr))

    expr = "{([<>])}"
    assert(verify_balanced_brackets(expr))

    code_snippet = """if (value == 10) {
                          print("Value is 10");
                      }
                   """
    assert(verify_balanced_brackets(code_snippet))

    assert(verify_balanced_brackets(""))

    expr = "]"
    assert(verify_balanced_brackets(expr) == False)

    expr = "]["
    assert(verify_balanced_brackets(expr) == False)

    expr = "([]]()"
    assert(verify_balanced_brackets(expr) == False)





if __name__ == "__main__":
    main()
