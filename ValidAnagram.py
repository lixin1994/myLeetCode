import collections


def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if s == t:
        return True
    if len(s) != len(t):
        return False
    for char in s:
        if char in t:
            t = t.replace(char, '', 1)
        else:
            return False
    return True
print(isAnagram("aacc", "ccac"))
print(collections.Counter("aacc"))
#print("asda".replace('a','',1))