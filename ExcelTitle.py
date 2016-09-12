import math
def convertToTitle(n):
        """
        :type n: int
        :rtype: str
        """
        strs = ''
        if n == 0:
            return strs
        m = int(math.log(n, 26))

        while m >= 0:
            strs += chr(n // 26 ** m + 64)
            n = n % 26 ** m
            m -= 1
        return strs

print(convertToTitle(26))
print(convertToTitle(702))