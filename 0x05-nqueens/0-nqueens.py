#!/usr/bin/python3
"""N Queens Module"""
import sys


n = len(sys.argv)
if n > 2 or n < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

def queens(n, i=0, a=[], b=[], c=[]):
    """Queens function"""
    if i < n:
        for k in range(n):
            if k not in a and i + k not in b and i - k not in c:
                yield from queens(n, i + 1, a + [k], b + [i + k], c + [i - k])
    else:
        yield a

def solve(n):
    """Solve function"""
    j = []
    i = 0
    for one in queens(n, 0):
        for two in one:
            j.append([i, two])
            i += 1
        print(j)
        j = []
        i = 0

solve(int(sys.argv[1]))
