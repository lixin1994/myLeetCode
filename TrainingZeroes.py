def trailingZeroes(n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        m = 5
        while m <= n:
            i = n // m
            result += i
            m = m ** 2

        return result

print(trailingZeroes(125))