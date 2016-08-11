def numTrees(n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1,1]

        for i in range (2, n + 1):
            temp = 0
            for j in range (0, i):
                temp += dp[j] * dp[i - 1 - j]
            dp.append(temp)
        return dp.pop()

print(numTrees(3))