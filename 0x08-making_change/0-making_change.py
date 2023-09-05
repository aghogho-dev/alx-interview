#!/usr/bin/python3
"""Make Change"""


def makeChange(coins, total):
    """make change func"""
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    n = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            n += 1

        if (total == 0):
            return n
    return -1
