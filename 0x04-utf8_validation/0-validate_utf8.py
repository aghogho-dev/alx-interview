#!/usr/bin/python3
"""UTF8 Validation."""


def validUTF8(data):
    """
    UTF8 Function
    """
    a = 1 << 7
    b = 1 << 6
    n = 0
    for i in data:
        c = 1 << 7
        if n == 0:
            while c & i:
                n += 1
                c = c >> 1
            if n == 0:
                continue
            if n == 1 or n > 4:
                return False
        else:
            if not (i & c and not (i & b)):
                return False
        n -= 1
    return not n
