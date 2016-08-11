import sys

import math


def numSquares(n):
    """
    :type n: int
    :rtype: int
    """
    base = int(math.sqrt(n))
    result = sys.maxint
    while base >= 1:
        if base ** 2 == n:
            return 1
        else:
            result = min(numSquares(n - base ** 2) + 1, result)
        base -= 1
    return result

print(numSquares(10))