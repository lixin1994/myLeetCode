from collections import deque

import math


def countNumbersWithUniqueDigits(n):
        """
        :type n: int
        :rtype: int
        """
        return int(sum([math.factorial(10)/math.factorial(10-i) for i in range(1, n + 1)]) * 0.9)
print(countNumbersWithUniqueDigits(10))
