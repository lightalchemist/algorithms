#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: heap_sort_big_files.py
Author: Hong-Wei Ng
Email: lightalchemist@gmail.com
Github: https://github.com/lightalchemist
Description: Qn 10.1 on pg 80 from Elements of Programming Interviews.

Given a number of files which contain lines of the form <timestamp>, ...
each sorted by timestamps,
combine the contents of all these files into a file sorted by the timestamps.

The individual files are of the order 5-100 MB and there may be many files.
Design an algorithm to perform the task that use very little RAM, ideally of
the order of a few KB.

"""

from heapq import heapify
from heapq import heappush
from heapq import heappop


def insert_line(heap, infile, fid):
    line = infile.readline()
    if line:
        timestamp = int(line.split(',')[0])
        heappush(heap, (timestamp, line, fid))


def sort(filenames, outfilename):
    with open(outfilename, 'w') as outfile:
        heap = []
        infiles = [open(f) for f in filenames]
        # Populate heap
        for i, infile in enumerate(infiles):
            insert_line(heap, infile, i)

        heapify(heap)

        while heap:
            timestamp, line, fid = heappop(heap)
            outfile.write(line)
            insert_line(heap, infiles[fid], fid)  # Replace line from file with another line from same file

        # Close all files
        for infile in infiles:
            infile.close()


def test():
    filenames = ["file1.txt", "file2.txt", "file3.txt"]
    outfilename = "sorted_lines.txt"
    sort(filenames, outfilename)


if __name__ == '__main__':
    test()
