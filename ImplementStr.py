def strStr(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0

        while i >= 0:
            j = 0
            while j >= 0:
                if j == len(needle):
                    return i
                if i + j == len(haystack):
                    return -1
                if haystack[i + j] != needle[j]:
                    break
                j += 1
            i += 1



a = "mississippi"
b = "mississippi"
print(strStr(a, b))