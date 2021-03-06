#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: balanced_brackets.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Check if brackets in given expression are balanced
"""


def is_balanced(expr):
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


def is_balanced2(expr):
    # This version can't handle ' and " because
    # it can't tell when it is meant to open and when to close
    # In principle it should be faster than is_balanced2
    # as it allows for early termination

    pair = {')': '(',
            ']': '[',
            # "'": "'",
            # '"': '"',
            '}': '{'}

    opening_brackets = set(pair.values())
    closing_brackets = set(pair.keys())
    stack = []
    for c in expr:
        if c in opening_brackets:
            stack.append(c)
        elif c in closing_brackets:
            if not stack:
                return False
            top = stack.pop()
            if pair.get(c, None) != top:
                return False

    # Make sure stack is empty at this point
    # and do not contain any leftover opening brackets
    return not stack


def main():
    expr = "([])[]()"
    assert(is_balanced2(expr))

    expr = "((([()]))())"
    assert(is_balanced2(expr))

    expr = "{([<>])}"
    assert(is_balanced2(expr))

    code_snippet = """if (value == 10) {
                          print("Value is 10");
                      }
                   """
    assert(is_balanced2(code_snippet))

    assert(is_balanced2(""))

    expr = "]"
    assert(is_balanced2(expr) == False)

    expr = "]["
    assert(is_balanced2(expr) == False)

    expr = "([]]()"
    assert(is_balanced2(expr) == False)





if __name__ == "__main__":
    main()
