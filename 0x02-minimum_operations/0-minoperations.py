#!/usr/bin/python3
"""Mimium operations."""


def minOperations(n: int) -> int:
    """
    Args:
      n (int)
    Returns: int
    """
    if n < 2:
        return 0
    
    p = 0
    q = 2
    while q <= n:
        if (n % q) == 0:
            p += q
            n /= q
            q -= 1
        q += 1
    return p
