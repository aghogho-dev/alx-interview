#!/usr/bin/python3
"""isprime game"""


def isWinner(x, nums):
    """isWinner"""
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    Ben, Maria = 0, 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    
    for i in range(2, len(a)):
        multiples(a, i)

    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    if Ben > Maria:
        return "Ben"
    elif Ben < Maria:
        return "Maria"
    else:
        return None


def multiples(ls, x):
    """Remove multiples"""
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (IndexError, ValueError):
            break
