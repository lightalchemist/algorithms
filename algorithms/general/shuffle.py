
"""
File: shuffle.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Perform in-place uniform shuffle of an array.
"""

import random


def shuffle(seq):
    for i in range(1, len(seq)):
        j = random.randint(0, i)
        seq[i], seq[j] = seq[j], seq[i]
