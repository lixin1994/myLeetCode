def grayCode(n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]
        for i in range(0, n):
            result.append(result[i] + 2 ** i)
        for j in range(0, n-1):
            result.append(result[j + i + 1] - 2 ** j)
        return result

print(grayCode(2))