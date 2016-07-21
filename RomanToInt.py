def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        romanDict = {'I' : 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        max = 0
        result = 0
        for i in s[::-1]:
            temp = romanDict[i]
            if temp >= max:
                result += temp
                max = temp
            else:
                result -= temp
        return result

print(romanToInt("MCD"))
